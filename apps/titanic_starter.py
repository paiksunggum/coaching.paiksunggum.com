import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv", encoding='cp949')
print(df.head())
print(df.shape)