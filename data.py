import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import zipfile

with zipfile.ZipFile("bank.zip", "r") as zip_ref:
    zip_ref.extractall("bank_data")

df = pd.read_csv("bank_data/bank.csv", sep = ';')
df.columns = df.columns.str.strip().str.replace('"', '')

print(df.head())

df = pd.read_csv('bank_data/bank.csv')
duplicates = df.duplicated()
print(f"found {duplicates.sum()} duplicate record")

clean_df = df.drop_duplicates()
print(f"dataset reduced from {len(df)} to {len(clean_df)} records")

#check for missing values 
print(df.isnull().sum())

