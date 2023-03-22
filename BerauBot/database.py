import pandas as pd

PATH_TO_FILE = 'D:\coding-lab-fast-track\selenium-bot\database.xlsx'

df = pd.read_excel(PATH_TO_FILE)
print(type(int(df['Tahun Masuk'][7])))
# for ind in df.index:
#     print(df['Site'][ind])