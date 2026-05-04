from pathlib import Path
import pandas as pd

csv_path = Path(__file__).parent / "Titanic-Dataset.csv"
df = pd.read_csv(csv_path)

print(df.head())
print("-" * 30)
print(df.shape)
print("-" * 30)
df.info()