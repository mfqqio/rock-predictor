#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main driver for creating features.

This script imports and calls functions containing logic that engineers
features from input data. Output is a dataframe of features for each hole.
"""

import pandas as pd
import numpy as np
import sys
<<<<<<< HEAD
from helpers.feature_eng import calc_penetration_rate, calc_prop_zero, calc_prop_max, calc_prop_half, count_oscillations
=======
from helpers.feature_eng import calc_penetration_rate, calc_prop_zero, calc_prop_max, calc_prop_half, class_distance
>>>>>>> jp_dev-week5

#### MAIN
# First check if command line arguments are provided before launching main script
# python src/create_features.py data/raw/sample_wide.csv data/intermediate/features.csv
if len(sys.argv) == 4:
    data_path = sys.argv[1]
    output_file_path = sys.argv[2]
    mode = sys.argv[3] # Mode can be "for_train" or "for_predict"

    # Read master joined data from file
    print('Reading joined input data...')
    df = pd.read_csv(data_path, low_memory=False)
    print('Master joined input data dimensions:', df.shape)

    # Column name mapping
    target_col='litho_rock_class'
    hole_id_col='hole_id'
    drilltime_col='DrillTime'
    operator_col='FirstName'
    hole_depth_col='depth'
    water_col = 'water'
    pulldown_col = 'pull'

    telem_features = ["hvib", "vvib", "pull",
    "air", "pos", "depth", "rot", "water"]

    #Create feature for second derivative of hole_depth progression
    df["pos_lagOfLag"] = df.pos_lag1_diff.diff().fillna(0)

    # For cases when exp_rock_type is "AIR" or "OB"
    df.exp_rock_class.fillna(value="Unknown", inplace=True)
    
    # Handle grouping for creating features for training (contains litho columns)
    # and for predict (does not contain litho columns/are blank)
    groupby_cols = []
    if mode == 'for_train':
        groupby_cols = ["hole_id", "exp_rock_type", "exp_rock_class", "litho_rock_type", "litho_rock_class"]
    elif mode == 'for_predict':
        groupby_cols = ["hole_id", "exp_rock_type", "exp_rock_class"]
        

    # Creating major dataframe with summarizing metrics for every hole
    features = (df.groupby(groupby_cols)
    .agg({"pos_lagOfLag": "median",
        "pos_lag1_diff": "median",
        "depth": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "air": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "pos": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "rot": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "utc_field_timestamp": "count",
        "ActualX": "mean",
        "ActualY": "mean",
        "hvib": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ("num_oscillations", count_oscillations),
                ],
        "vvib": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ("num_oscillations", count_oscillations),
                ],
<<<<<<< HEAD
        "water": ["std", "max", "min", "sum", "median",
                  ("prop_zero", calc_prop_zero)],
        "pull": [("prop_max", calc_prop_max),
                 ("prop_half", calc_prop_half),
                 ("num_oscillations",count_oscillations)],
        "rot": ["std", "max", "min", "sum", "median",
                ("num_oscillations", count_oscillations)],
        "air": ["std", "max", "min", "sum", "median",
                ("num_oscillations", count_oscillations)]
=======
        "pull": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "air": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "pos": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "depth": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "rot": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "water": ["std", "max", "min", "sum", "median",
                ("10th_quant", lambda x: x.quantile(0.1)),
                ("25th_quant", lambda x: x.quantile(0.25)),
                ("75th_quant", lambda x: x.quantile(0.75)),
                ("90th_quant", lambda x: x.quantile(0.9)),
                ],
        "water": [calc_prop_zero],
        "pull": [calc_prop_max, calc_prop_half]
>>>>>>> jp_dev-week5
        })
        .reset_index()
    )
    features.columns = ['_'.join(col).strip() if col[1] != "" else col[0] for col in features.columns.values]
    features.rename(columns={"utc_field_timestamp_count": "time_count"},
                    inplace=True)
    features["penetration_rate"] = calc_penetration_rate(features.depth_max,
                                                         features.depth_min,
                                                         features.time_count)

    #Add one hot encoding for Exploration Rock Type
    features["exp_rock_type_onehot"] = features.exp_rock_type
    features = pd.get_dummies(data=features, columns=["exp_rock_type_onehot"])

    # Add dist features
    a = class_distance(features)
    features = pd.concat([features, a], axis = 1)

    # Output calculated features to file
    features.to_csv(output_file_path, index=False)

    print('Features calculated and written to file:', output_file_path)
