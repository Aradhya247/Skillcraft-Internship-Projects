import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('Salary_Data.csv')
print(df.head())
print(df.columns)

age_data = df['Age'].dropna()

plt.figure(figsize=(10, 6))
plt.hist(age_data, bins=20, color='skyblue', edgecolor='green')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()