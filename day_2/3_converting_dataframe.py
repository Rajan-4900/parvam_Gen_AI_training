# converting the train.txt file into a DataFrame using pandas

import pandas as pd

# Convert the semicolon-separated text file into a DataFrame
df = pd.read_csv("train.txt", sep=";", names=["text", "emotion"], header=None)

print("\nFirst 5 rows:")
print(df.head(5)) # first 5 rows of the DataFrame

print()

# print(df.tail(5)) # last 5 rows

# count null values
print("\nNull values in each column:")
print(df.isnull().sum()) # count of null values in each column

print()

#drop null values
df = df.dropna()
print(df.isnull().sum()) # count of null values after dropping