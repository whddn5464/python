import pandas as pd
CCTV_Seoul = pd.read_csv('C:/Users/kim96/Desktop/program/python/data/01. CCTV_in_Seoul.csv',  encoding='utf-8')
CCTV_Seoul.head()
CCTV_Seoul.columns
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()