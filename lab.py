import pandas as pd
import numpy as np

PATH_TO_FILE = 'D:\coding-lab-fast-track\Bot\excel\WTP.xlsx'
df = pd.read_excel(PATH_TO_FILE)
print(df.iloc[391])
