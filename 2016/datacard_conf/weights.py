from Tools.Weights.Weights import Weight

lumi = Weight("35.87",[])
lumikit = Weight("35870",[])

weight = Weight("(weight)",["weight"])
emb_weight = Weight("weight",["weight"])

tauidsft_1 = Weight( "( 0.95*(gen_match_1 == 5) + 1.0*(gen_match_1 !=5) )", ["gen_match_1"] )
tauidsft_2 = Weight( "( 0.95*(gen_match_2 == 5) + 1.0*(gen_match_2 !=5) )", ["gen_match_2"] )
tauidsft = tauidsft_1 + tauidsft_2

mt_sel = Weight("( gen_match_1 == 4 & gen_match_2 == 5 )", ["gen_match_1","gen_match_2"])
et_sel = Weight("( gen_match_1 == 3 & gen_match_2 == 5 )", ["gen_match_1","gen_match_2"])
tt_sel = Weight("( gen_match_1 == 5 & gen_match_2 == 5 )", ["gen_match_1","gen_match_2"])

zptweight = Weight( "zPtReweightWeight", ["zPtReweightWeight"] )
topweight = Weight( "topWeight_run1", ["topWeight_run1"] )
gghweight = Weight( "ggh_NNLO_weight", ["ggh_NNLO_weight"] )

prefire =   Weight(" (0.972+0.011*(jpt_1>0)*(jpt_1<200)*(njets<2 | ((jdeta<2.8 | mjj<400) & (mjj<60 | mjj>=120)))-0.52*(jpt_1>=200)) ",["jpt_1","njets","jdeta","mjj"])

bbH_correction = Weight("1.01",[])

signals_ggh = ["ggH125",
           "ggH_VBFTOPO_JET3VETO125",
           "ggH_VBFTOPO_JET3125",
           "ggH_0J125",
           "ggH_1J_PTH_0_60125",
           "ggH_1J_PTH_60_120125",
           "ggH_1J_PTH_120_200125",
           "ggH_1J_PTH_GT200125",
           "ggH_GE2J_PTH_0_60125",
           "ggH_GE2J_PTH_60_120125",
           "ggH_GE2J_PTH_120_200125",
           "ggH_GE2J_PTH_GT200125"
            ]
signals_qqh = ["qqH125",
                "qqH_VBFTOPO_JET3VETO125", "qqH_VBFTOPO_JET3125", "qqH_REST125",
                "qqH_PTJET1_GT200125", "qqH_VH2JET125"]

signals_VH = ["WH125","ZH125"]

signals = signals_ggh + signals_qqh + signals_VH

config = {

    "template_weight":{
        "mt":{
            "Z":      lumi + weight + tauidsft + zptweight,
            "EMB":    emb_weight + mt_sel,
            "W":      lumi + weight + tauidsft,
            "TT":     lumi + weight + tauidsft + topweight,
            "VV":     lumi + weight + tauidsft,
            "ggH125": lumikit + weight + gghweight + tauidsft + bbH_correction,
            "qqH125": lumikit + weight + tauidsft + prefire,
            "WH125":  lumikit + weight + tauidsft,
            "ZH125":  lumikit + weight + tauidsft 
        },
        "et":{
             "Z":      lumi + weight + tauidsft + zptweight,
            "EMB":    emb_weight + et_sel,
            "W":      lumi + weight + tauidsft,
            "TT":     lumi + weight + tauidsft + topweight,
            "VV":     lumi + weight + tauidsft,
            "ggH125": lumikit + weight + gghweight + tauidsft + bbH_correction,
            "qqH125": lumikit + weight + tauidsft + prefire,
            "WH125":  lumikit + weight + tauidsft,
            "ZH125":  lumikit + weight + tauidsft       
        },
        "tt":{
            "Z":      lumi + weight + tauidsft + zptweight,
            "EMB":    emb_weight + tt_sel,
            "W":      lumi + weight + tauidsft,
            "TT":     lumi + weight + tauidsft + topweight,
            "VV":     lumi + weight + tauidsft,
            "ggH125": lumikit + weight + gghweight + tauidsft + bbH_correction,
            "qqH125": lumikit + weight + tauidsft + prefire,
            "WH125":  lumikit + weight + tauidsft,
            "ZH125":  lumikit + weight + tauidsft        
        }
    },
    "reweighting":{
        "general":{
            "apply_to":["all"],
            "weights":{
                "CMS_scale_met_unclusteredUp"         : Weight("",[]),
                "CMS_scale_met_unclusteredDown"       : Weight("",[]),
                "CMS_htt_eff_b_Run2016Up"             : Weight("",[]),
                "CMS_htt_eff_b_Run2016Down"           : Weight("",[]),
                "CMS_htt_mistag_b_Run2016Up"          : Weight("",[]),
                "CMS_htt_mistag_b_Run2016Down"        : Weight("",[]),
                "CMS_htt_boson_scale_metUp"           : Weight("",[]),
                "CMS_htt_boson_scale_metDown"         : Weight("",[]),
                "CMS_htt_boson_reso_metUp"            : Weight("",[]),
                "CMS_htt_boson_reso_metDown"          : Weight("",[])
            }
        },
        "ttbar_all":{
            "apply_to":["TT","TTT","TTJ","TTL"],
            "weights":{
                "CMS_htt_ttbarShapeUp"                : Weight("topWeight_run1",["topWeight_run1"]),
                "CMS_htt_ttbarShapeDown"              : Weight("(1.0 / topWeight_run1)",["topWeight_run1"]),
            }
        },
        "dy_all":{
            "apply_to":["Z","ZTT","ZJ","ZL"],
            "weights":{
                "CMS_htt_dyShape_Run2016Up"                   : Weight("zPtReweightWeight",["zPtReweightWeight"]),
                "CMS_htt_dyShape_Run2016Down"                 : Weight("(1.0 / zPtReweightWeight)",["zPtReweightWeight"]),
            }
        },
        "embedding_uncertainties":{
            "apply_to":["EMB"],
            "weights":{
                "CMS_3ProngEff_Run2016Up"                   : Weight("(embeddedDecayModeWeight_effUp_pi0Nom   / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effUp_pi0Nom"] ),
                "CMS_3ProngEff_Run2016Down"                 : Weight("(embeddedDecayModeWeight_effDown_pi0Nom / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effDown_pi0Nom"] ),                
                "CMS_1ProngPi0Eff_Run2016Up"                : Weight("(embeddedDecayModeWeight_effNom_pi0Up   / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effNom_pi0Up"] ),
                "CMS_1ProngPi0Eff_Run2016Down"              : Weight("(embeddedDecayModeWeight_effNom_pi0Down / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effNom_pi0Down"] ),
                "CMS_3ProngEffUp"                           : Weight("(embeddedDecayModeWeight_effUp_pi0Nom   / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effUp_pi0Nom"] ),
                "CMS_3ProngEffDown"                         : Weight("(embeddedDecayModeWeight_effDown_pi0Nom / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effDown_pi0Nom"] ),                
                "CMS_1ProngPi0EffUp"                        : Weight("(embeddedDecayModeWeight_effNom_pi0Up   / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effNom_pi0Up"] ),
                "CMS_1ProngPi0EffDown"                      : Weight("(embeddedDecayModeWeight_effNom_pi0Down / embeddedDecayModeWeight)", ["embeddedDecayModeWeight","embeddedDecayModeWeight_effNom_pi0Down"] )
            }
        },        
        # "genuine_taus":{
        #     "apply_to":["ZTT","TTT","VVT","TTL","VVL","ZL","EMB","ggH125","qqH125"],
        #     "weights":{
        #         "CMS_scale_t_1prong_Run2016Up"                : Weight("",[]),
        #         "CMS_scale_t_1prong_Run2016Down"              : Weight("",[]),
        #         "CMS_scale_t_1prong1pizero_Run2016Up"         : Weight("",[]),
        #         "CMS_scale_t_1prong1pizero_Run2016Down"       : Weight("",[]),
        #         "CMS_scale_t_3prong_Run2016Up"                : Weight("",[]),
        #         "CMS_scale_t_3prong_Run2016Down"              : Weight("",[])
        #     }
        # },
        "jet_fakes":{
            "apply_to":["ZJ","TTJ","VVJ","W"],
            "weights":{
                "CMS_htt_jetToTauFake_Run2016Up"              :{
                    "et": Weight("((1-0.002*pt_2)*(pt_2 < 200) + 0.6*(pt_2 >= 200))", ["pt_2"]),
                    "mt": Weight("((1-0.002*pt_2)*(pt_2 < 200) + 0.6*(pt_2 >= 200))", ["pt_2"]),
                    "tt": Weight("(( (1-0.002*pt_1)*(pt_1 < 200) + 0.6*(pt_1 >= 200) ) * ( (1-0.002*pt_2)*(pt_2 < 200) + 0.6*(pt_2 >= 200) ) )", ["pt_1","pt_2"])
                },
                "CMS_htt_jetToTauFake_Run2016Down"            :{
                   "et": Weight("((1+0.002*pt_2)*(pt_2 < 200) + 1.4*(pt_2 >= 200))", ["pt_2"]),
                   "mt": Weight("((1+0.002*pt_2)*(pt_2 < 200) + 1.4*(pt_2 >= 200))", ["pt_2"]),
                   "tt": Weight("(( (1+0.002*pt_1)*(pt_1 < 200) + 1.4*(pt_1 >= 200) ) * ( (1-0.002*pt_2)*(pt_2 < 200) + 1.4*(pt_2 >= 200) ) )", ["pt_1","pt_2"])
                },
                "CMS_scale_j_Run2016Up"                       : Weight("",[]),
                "CMS_scale_j_Run2016Down"                     : Weight("",[])                
            }
        },
#        "lepton_fakes":{
#            "apply_to":["ZL"],
#            "weights":{
#                "CMS_ZLShape_mt_1prong_Run2016Up"             : Weight("",[]),
#                "CMS_ZLShape_mt_1prong_Run2016Down"           : Weight("",[]),
#                "CMS_ZLShape_mt_1prong1pizero_Run2016Up"      : Weight("",[]),
#                "CMS_ZLShape_mt_1prong1pizero_Run2016Down"    : Weight("",[]),
#                "CMS_ZLShape_et_1prong_Run2016Up"             : Weight("",[]),
#                "CMS_ZLShape_et_1prong_Run2016Down"           : Weight("",[]),
#                "CMS_ZLShape_et_1prong1pizero_Run2016Up"      : Weight("",[]),
#                "CMS_ZLShape_et_1prong1pizero_Run2016Down"    : Weight("",[])        
#            }
#        },
        "trigger_lepton_legs_mc":{
            "apply_to":["ZTT", "ZL", "ZJ", "W", "TTT", "TTL", "TTJ", "VVL", "VVT", "VVJ"] + signals,
            "weights":{
                "CMS_eff_trigger_mt_Run2016Up":             Weight("(1.0*(pt_1<=23)+1.02*(pt_1>23))",["pt_1"]),
                "CMS_eff_trigger_mt_Run2016Down":           Weight("(1.0*(pt_1<=23)+0.98*(pt_1>23))",["pt_1"]),
                "CMS_eff_xtrigger_mt_Run2016Up":            Weight("(1.054*(pt_1<=23)+1.0*(pt_1>23))",["pt_1"]),
                "CMS_eff_xtrigger_mt_Run2016Down":          Weight("(0.946*(pt_1<=23)+1.0*(pt_1>23))",["pt_1"]),
                "CMS_eff_trigger_et_Run2016Up":             Weight("(1.0*(pt_1<=28)+1.02*(pt_1>28))",["pt_1"]),
                "CMS_eff_trigger_et_Run2016Down":           Weight("(1.0*(pt_1<=28)+0.98*(pt_1>28))",["pt_1"]),
                "CMS_eff_xtrigger_et_Run2016Up":            Weight("(1.054*(pt_1<=28)+1.0*(pt_1>28))",["pt_1"]),
                "CMS_eff_xtrigger_et_Run2016Down":          Weight("(0.946*(pt_1<=28)+1.0*(pt_1>28))",["pt_1"]),
            }
        },
        "trigger_lepton_legs_emb":{
            "apply_to":["EMB"],
            "weights":{
                "CMS_eff_trigger_emb_mt_Run2016Up":             Weight("(1.0*(pt_1<=23)+1.02*(pt_1>23))",["pt_1"]),
                "CMS_eff_trigger_emb_mt_Run2016Down":           Weight("(1.0*(pt_1<=23)+0.98*(pt_1>23))",["pt_1"]),
                "CMS_eff_xtrigger_emb_mt_Run2016Up":            Weight("(1.054*(pt_1<=23)+1.0*(pt_1>23))",["pt_1"]),
                "CMS_eff_xtrigger_emb_mt_Run2016Down":          Weight("(0.946*(pt_1<=23)+1.0*(pt_1>23))",["pt_1"]),
                "CMS_eff_trigger_emb_et_Run2016Up":             Weight("(1.0*(pt_1<=28)+1.02*(pt_1>28))",["pt_1"]),
                "CMS_eff_trigger_emb_et_Run2016Down":           Weight("(1.0*(pt_1<=28)+0.98*(pt_1>28))",["pt_1"]),
                "CMS_eff_xtrigger_emb_et_Run2016Up":            Weight("(1.054*(pt_1<=28)+1.0*(pt_1>28))",["pt_1"]),
                "CMS_eff_xtrigger_emb_et_Run2016Down":          Weight("(0.946*(pt_1<=28)+1.0*(pt_1>28))",["pt_1"]),
            }
        },        
        "ggFWG1Uncertainties":{
            "apply_to": signals_ggh,
            "weights":{
                "THU_ggH_MuUp":      Weight("THU_ggH_Mu",["THU_ggH_Mu"] ),
                "THU_ggH_MuDown":    Weight("(1.0 / THU_ggH_Mu)",["THU_ggH_Mu"] ),
                "THU_ggH_ResUp":     Weight("THU_ggH_Res",["THU_ggH_Res"] ),
                "THU_ggH_ResDown":   Weight("(1.0 / THU_ggH_Res)",["THU_ggH_Res"] ),
                "THU_ggH_Mig01Up":   Weight("THU_ggH_Mig01",["THU_ggH_Mig01"] ),
                "THU_ggH_Mig01Down": Weight("(1.0 / THU_ggH_Mig01)",["THU_ggH_Mig01"] ),
                "THU_ggH_Mig12Up":   Weight("THU_ggH_Mig12",["THU_ggH_Mig12"] ),
                "THU_ggH_Mig12Down": Weight("(1.0 / THU_ggH_Mig12)",["THU_ggH_Mig12"] ),
                "THU_ggH_VBF2jUp":   Weight("THU_ggH_VBF2j",["THU_ggH_VBF2j"] ),
                "THU_ggH_VBF2jDown": Weight("(1.0 / THU_ggH_VBF2j)",["THU_ggH_VBF2j"] ),
                "THU_ggH_VBF3jUp":   Weight("THU_ggH_VBF3j",["THU_ggH_VBF3j"] ),
                "THU_ggH_VBF3jDown": Weight("(1.0 / THU_ggH_VBF3j)",["THU_ggH_VBF3j"] ),
                "THU_ggH_PT60Up":    Weight("THU_ggH_PT60",["THU_ggH_PT60"] ),
                "THU_ggH_PT60Down":  Weight("(1.0 / THU_ggH_PT60)",["THU_ggH_PT60"] ),
                "THU_ggH_PT120Up":   Weight("THU_ggH_PT120",["THU_ggH_PT120"] ),
                "THU_ggH_PT120Down": Weight("(1.0 / THU_ggH_PT120)",["THU_ggH_PT120"] ),
                "THU_ggH_qmtopUp":   Weight("THU_ggH_qmtop",["THU_ggH_qmtop"] ),
                "THU_ggH_qmtopDown": Weight("(1.0 / THU_ggH_qmtop)",["THU_ggH_qmtop"] )
            }

        }
    }
}
