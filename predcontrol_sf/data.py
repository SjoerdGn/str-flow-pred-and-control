from dataclasses import dataclass
import pandas as pd

@dataclass
class DataCase:
    discharge: pd.DataFrame