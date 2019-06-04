import pytest
import numpy as np
import pandas as pd
import os
import sys

# By default, python only searches for packages and modules to import
# from the directories listed in sys.path
# The idea is to add another path that inlcudes the function we want to test
# This allows us to import that function
#sys.path.append("/ubc_drilltelemetry/pipeline/src/helpers")
# os.path.dirname(os.path.dirname(os.path.realpath("./pipeline/src/helpers"))))
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
# Now that we have added the path, we can import the function we want to test
from src.helpers.feature_eng import calc_penetration_rate

# Dummy input vector
vec_max_depth = np.array([10.0,40.0,75.0])
vec_min_depth = np.array([0,0,0])
vec_count_time = np.array([10,20,25])
expected_rate = np.array([1.0, 2.0, 3.0])

# Let's get the output of our function with the test vector



# Test to check if the output matches expectations using sample vector
def test_calc_penetration_rate_output():
    result = calc_penetration_rate(vec_max_depth, vec_min_depth, vec_count_time)
    assert np.array_equal(result, expected_rate), "Failed to achieve expected rate"
