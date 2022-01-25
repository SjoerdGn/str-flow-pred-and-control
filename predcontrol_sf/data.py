from dataclasses import dataclass
import pandas as pd
import numpy as np

@dataclass
class DataCase:
    discharge: pd.DataFrame
    # TODO: implement data for case object

def handle_float_or_array_like(x):
    if type(x) == int or float:
        d = np.array([x])
    else:
        d = np.copy(x)
    return d

def check_non_negative_discharge(x):
    if np.sum(x < 0) > 0:
        raise ValueError("Found negative discharge")

def return_discharge(discharge, d):
    if type(discharge) == int or float:
        d = d[0]
    return d