config = {
	"categories":{
		"mt":{
			"inclusive":               {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT-"},
			"ggh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0"},
			"ggh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==101"},
			"ggh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==102"},
			"ggh_0J":                  {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==103"},
			"ggh_1J_PTH_0_60":         {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==104"},
			"ggh_1J_PTH_60_120":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==105"},
			"ggh_1J_PTH_120_200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & ( htxs_reco_ggf==106 || htxs_reco_ggf==107 )"},
			# "ggh_1J_PTH_GT200":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==107"},
			"ggh_GE2J_PTH_0_60":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==108"},
			"ggh_GE2J_PTH_60_120":     {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==109"},
			"ggh_GE2J_PTH_120_200":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & ( htxs_reco_ggf==110 || htxs_reco_ggf==111 )"},
			# "ggh_GE2J_PTH_GT200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==111"},
			"qqh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1"},
			"qqh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==201"},
			"qqh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==202"},
			"qqh_VH2JET":        	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==203"},
			"qqh_REST":        	   	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==204"},
			"qqh_PTJET1_GT200":    	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==205"},
			"ztt":   				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 2"},
			"zll":   				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 3"},
			"w":     				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 4"},
			"tt":    				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 5"},
			"ss":    				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 6"},
			"misc":  				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 7"}
		},

		"et":{
			"inclusive":               {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT-"},
			"ggh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0"},
			"ggh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==101"},
			"ggh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==102"},
			"ggh_0J":                  {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==103"},
			"ggh_1J_PTH_0_60":         {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==104"},
			"ggh_1J_PTH_60_120":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==105"},
			"ggh_1J_PTH_120_200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & ( htxs_reco_ggf==106 || htxs_reco_ggf==107 )"},
			# "ggh_1J_PTH_GT200":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==107"},
			"ggh_GE2J_PTH_0_60":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==108"},
			"ggh_GE2J_PTH_60_120":     {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==109"},
			"ggh_GE2J_PTH_120_200":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & ( htxs_reco_ggf==110 || htxs_reco_ggf==111 )"},
			# "ggh_GE2J_PTH_GT200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==111"},
			"qqh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1"},
			"qqh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==201"},
			"qqh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==202"},
			"qqh_VH2JET":        	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==203"},
			"qqh_REST":        	   	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==204"},
			"qqh_PTJET1_GT200":    	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==205"},
			"ztt":   				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 2"},
			"zll":   				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 3"},
			"w":     				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 4"},
			"tt":    				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 5"},
			"ss":    				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 6"},
			"misc":  				   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 7"}
		},
		"tt":{
			"inclusive":               {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT-"},
			"ggh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0"},
			"ggh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==101"},
			"ggh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==102"},
			"ggh_0J":                  {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==103"},
			"ggh_1J_PTH_0_60":         {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==104"},
			"ggh_1J_PTH_60_120":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==105"},
			"ggh_1J_PTH_120_200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==106"},
			"ggh_1J_PTH_GT200":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==107"},
			"ggh_GE2J_PTH_0_60":       {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==108"},
			"ggh_GE2J_PTH_60_120":     {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==109"},
			"ggh_GE2J_PTH_120_200":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==110"},
			"ggh_GE2J_PTH_GT200":      {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 0 & htxs_reco_ggf==111"},
			"qqh":					   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1"},
			"qqh_VBFTOPO_JET3VETO":    {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==201"},
			"qqh_VBFTOPO_JET3":        {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==202"},
			"qqh_VH2JET":        	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==203"},
			"qqh_REST":        	   	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==204"},
			"qqh_PTJET1_GT200":    	   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 1 & htxs_reco_vbf==205"},
			"ztt":      			   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 2"},
			"noniso":   			   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 3"},
			"misc":     			   {"":  "-TRIG- & -VETO- & -ISO- & -OS- & -MT- & predicted_class == 4"}
		}
	}
}
