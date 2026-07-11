import pandas as pd

df = pd.read_csv("data.csv")

# print(df) #truncted version (first and last 5 rows)
print(df.to_string()) #prints everything