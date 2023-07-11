"""
This example performs a fully controlled electrolyzer simulation using the
`run_electrolyzer` function. See `example_run.ipynb` for an interactive option.
"""
import os

import pandas as pd
import numpy as np

from electrolyzer import run_electrolyzer


fname_input_modeling = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "modeling_options.yaml"
)

turbine_rating = 5.0  # MW

# Create cosine test signal
test_signal_angle = np.linspace(0, 8 * np.pi, 3600 * 8 + 10)
base_value = (turbine_rating / 2) + 0.2
variation_value = turbine_rating - base_value
power_test_signal = (base_value + variation_value * np.cos(test_signal_angle)) * 1e6

t_span = 50000 # hours
power_test_signal = base_value * np.ones(t_span) * 1e6 # W

elec, results_df = run_electrolyzer(fname_input_modeling, power_test_signal)
print(results_df.head())
# print(res)
