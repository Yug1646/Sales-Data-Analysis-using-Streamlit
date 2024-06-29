import Exception_Handling as e
import pandas as pd

def save_file(df):
    try:
        df.to_csv('Amazon2_Raw.csv')
    except:
        raise e.SaveFile

def load_file(file = 'Amazon2_Raw.csv'):
    try:
        df = pd.read_csv(file)
        return df
    except:
        raise e.NoFile