import json
import pandas
import root_pandas as rp
import os
import sys
import yaml
from helper import calc

def main():

    SR = Reader("mt","conf/global_config_2017.json",2)
    with open("dump.json","w") as FSO:
        json.dump(SR.config, FSO, indent = 4, sort_keys=True )

class Reader():

    def __init__(self, channel,config_file, folds):
        self.itersamples = []
        self.idx = 0

        self.channel = channel
        self.trainReweighting = ""
        self.folds = folds
        self.processes = []
        self.needToAddVars = []

        with open("conf/hist_names.json","r") as FSO:
            self.hist_names = json.load(FSO)

        with open("conf/cuts.json","r") as FSO:
            cuts = json.load(FSO)
            for c in cuts:
                cuts[c] = self._assertChannel( cuts[c] )
            self.cut_dict = cuts
        self.config_file = config_file
        self.config = self._flattenConfig()


    def __iter__(self):
        return self

    def next(self):
        try:
            sample = self.itersamples[ self.idx ]
            self.idx += 1
            return self.loadForMe( sample ), sample["histname"]
        except IndexError as e:
            raise StopIteration


    def _flattenConfig(self):
        '''
        Read dataset configuration file and flatten the return object to the current use case.
        '''
        try:
            with open(self.config_file,"r") as FSO:
                config = json.load(FSO)
        except ValueError as e:
            print e
            print "Check {0}. Probably a ',' ".format(self.config_file)
            sys.exit(0)

        targets = []
        config["channel"] = self.channel
        config["target_names"] = {}
        config["variables"] = self._assertChannel( config["variables"] )
        config["version"] = self._assertChannel( config["version"] )
        # if self.channel == "mt":

        config["path"] = "{path}/{version}".format( **config )

        for sample in config["samples"]:
            
            snap = config["samples"][sample]
            self.processes.append(sample)

            sample_name = self._assertChannel( snap["name"] )
            snap["target"] = self._assertChannel(snap["target"] )
            targets.append( snap["target"]  )

            snap["name"]    = "{path}/{channel}-{name}.root".format(name = sample_name, **config)
            snap["select"] = self._parseCut( snap["select"] )

            snap["train_weight_scale"] = self._assertChannel( snap["train_weight_scale"] )
            snap["event_weight"]  = self._assertChannel( snap["event_weight"] )
            
            if sample != "data" and sample != "estimate":
                snap["shapes"]  = self._getShapePaths( snap["name"], sample )
                if type(snap["event_weight"]) is list:
                    config["addvar"] = list( set( config["addvar"] + snap["event_weight"] ) )

            config["samples"][sample] = snap

        targets.sort()
        targets = [ t for t in targets if t != "none" ]
        target_map = {"none":-1}

        for i,t in enumerate(set(targets)):
            config["target_names"][i] = t
            target_map[t] = i

        for sample in config["samples"]:
            config["samples"][sample]["target"]  = target_map.get( config["samples"][sample]["target"], -1 )  

        return config


    def getSamplesForTraining(self):
        self.setNominalSamples()
        samples = []
        for sample,histname in self:
            samples.append(sample)
        print "Combining for training"
        return self.combineFolds(samples)

    def setNominalSamples(self):
        self.itersamples = []
        self.idx = 0
        samples = self.config["samples"].keys()
        samples.sort()
        for sample in samples:
            if sample == "data" or "_more" in sample: continue

            tmp = self._getCommonSettings(sample)

            tmp["path"] = self.config["samples"][sample]["name"] 
            tmp["histname"   ] = sample
            tmp["rename"      ] = {}

            self.itersamples.append( tmp )

        return self

    def setFullSamples(self, add_jec = False):
        self.itersamples = []
        self.idx = 0
        samples = self.config["samples"].keys()
        samples.sort()
        for sample in samples:
            if "_full" in sample:

                tmp = self._getCommonSettings(sample)
                tmp["path"] = self.config["samples"][sample]["name"] 
                tmp["histname"   ] = sample
                tmp["rename"      ] = {}
                self.itersamples.append( tmp )

                if add_jec and not "data" in sample:
                    for shape in self.config["samples"][sample]["shapes"]:
                        if not "Total" in shape: continue

                        tmp = self._getCommonSettings(sample)

                        tmp["path"] = self.config["samples"][sample]["shapes"][shape] 
                        tmp["histname"   ] = sample.replace("full",shape)
                        tmp["rename"      ] = self._getRenaming( shape )

                        self.itersamples.append( tmp )                

        return self

    def setTESSamples(self):
        self.itersamples = []
        self.idx = 0
        samples = self.config["samples"].keys()
        samples.sort()
        for sample in samples:
            if "data" in sample or not "_full" in sample: continue

            for shape in self.config["samples"][sample]["shapes"]:
                if not "TES" in shape: continue

                tmp = self._getCommonSettings(sample)

                tmp["path"] = self.config["samples"][sample]["shapes"][shape]
                if not tmp["path"]: continue

                tmp["histname"   ] = sample.replace("full",shape)
                tmp["rename"      ] = {}

                self.itersamples.append( tmp )

        return self

    def loadForMe(self, sample_info):

        print "Loading ",sample_info["histname"] , sample_info["path"].split("/")[-1]
        DF = self._getDF(sample_path = sample_info["path"], 
                          select = sample_info["select"])
        DF.eval( "event_weight = " + sample_info["event_weight"], inplace = True  )
        DF["target"] = sample_info["target"]

        if not self.config["train_weight"]:
            DF["train_weight"] = 1.0
        else:
            DF["train_weight"] = self._getTrainWeight(DF, scale = sample_info["train_weight_scale"] )

        if sample_info["rename"]:
            DF.rename(columns = sample_info["rename"], inplace = True)



        return self._getFolds( DF )

    def combineFolds(self, samples):

        folds = [ [fold] for fold in samples[0] ]
        for sample in samples[1:]:
            for i in xrange(len(folds)):
                folds[i].append( sample[i] )

        for i,fold in enumerate(folds): 
            folds[i] = pandas.concat( fold, ignore_index=True).sample(frac=1., random_state = 41).reset_index(drop=True)

        return folds

    def get(self, what, add_jec = False):
        if what == "nominal"  : return self.setNominalSamples()
        if what == "full"     : return self.setFullSamples(add_jec)
        if what == "tes"      : return self.setTESSamples()

    def _parseCut(self, cutstring):
        cutstring = self._assertChannel( cutstring )
        for alias,cut in self.cut_dict.items():
            cutstring = cutstring.replace( alias, cut )
        return cutstring

    def _assertChannel(self, entry):

        if type( entry ) is dict:
            return entry[ self.channel ]
        else:
            return entry      

    def _getShapePaths(self, path, sample):

        shapes = {"TES1p0p0Up":"","TES1p0p0Down":"","TES1p1p0Up":"","TES1p1p0Down":"","TES3p0p0Up":"","TES3p0p0Down":"","TotalUp":sample,"TotalDown":sample}

        for shape in shapes:
            if ("ZL" in shape and sample != "ZL") or ("ZL" in shape and self.channel == "tt"): continue
            if sample in ["W","TTJ","ZJ","VVJ"] and not shape in ["JECUp","JECDown"]: continue
            shape_path = path.replace("NOMINAL",shape )
            if os.path.exists( shape_path ):
                shapes[shape] = shape_path
            else:
                shapes[shape] = path

        return shapes

    def _getCommonSettings(self, sample):

        settings = {}
        settings["event_weight"] = self._getEventWeight(sample)
        settings["target"      ] = self.config["samples"][sample]["target"] 
        settings["select"      ] = self.config["samples"][sample]["select"]
        settings["train_weight_scale"] = self.config["samples"][sample]["train_weight_scale"]
        
        return settings


    def _getEventWeight(self, sample):
        if type( self.config["samples"][sample]["event_weight"] ) is list:
            return "*".join( self.config["samples"][sample]["event_weight"] + [ str(self.config["lumi"]) ] )

        if type( self.config["samples"][sample]["event_weight"] ) is float:
            return str( self.config["samples"][sample]["event_weight"] )

        if type( self.config["samples"][sample]["event_weight"] ) is unicode:
            return "*".join(["1000", str( self.config["samples"][sample]["event_weight"] ), str(self.config["lumi"]) ])

        else:
            return 1.0

    def _getTrainWeight(self, DF, scale):
        if self.config["train_weight"] == "normalize_evt":
            evts = len(DF)
            if evts > 0: return 10000 / float(evts)

        elif self.config["train_weight"] == "normalize_xsec":
            return DF["event_weight"].sum() 

        elif self.config["train_weight"] == "use_scale":
            return DF["event_weight"].abs() * scale

        else:
            return 1.0

    def _getRenaming(self, corr):

        tmp =[]
        for nom in ["njets"]:
            if not nom == "jpt": tmp+= [(nom, nom+corr),(nom+corr, nom) ]
            else : tmp += [ (nom + "_1", nom+corr+ "_1"),(nom+corr+ "_1", nom+ "_1"),
                            (nom + "_2", nom+corr+ "_2"),(nom+corr+ "_2", nom+ "_2") ]

        return dict( tmp )

    def _getFolds(self, df):

        if self.folds != 2: raise NotImplementedError("Only implemented two folds so far!!!")
        folds = []

        folds.append( df.query( "entry % 2 != 0 " ).reset_index(drop=True) )
        folds.append( df.query( "entry % 2 == 0 " ).reset_index(drop=True) )

        return folds

    def _getDF( self, sample_path, select ):
        branches = set( self.config["variables"] + self.config["addvar"] )
        tmp = rp.read_root( paths = sample_path,
                             where = select,
                             columns = branches)

        if self.needToAddVars:
            for new in self.needToAddVars:
                tmp[new] = tmp.apply( calc(new), axis=1 )

        tmp.replace(-999.,-10, inplace = True)

        return tmp



if __name__ == '__main__':
    main()
