# Load data for training and running

import pandas as pd

def load_data_bom_aus(path) -> pd.DataFrame:
    data = pd.read_csv(path,
                       comment='#')
    data.columns = ['date', 'Value','Quality Code','Interpolation Type']
    data.index = pd.to_datetime(data['date'])
    data = data.drop(columns='date')
    return data