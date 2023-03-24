import pandas as pd

PATH_TO_FILE = r'D:\coding-lab-fast-track\Bot\excel\Penerima Manfaat Trading Gabah.xlsx'

df = pd.read_excel(PATH_TO_FILE)
print(df.columns)

# for ind in df.index:
#     print(df['Site'][ind])