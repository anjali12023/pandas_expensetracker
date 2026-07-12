import pandas as pd

# df = pd.read_csv("data.csv")

# print(df) #truncted version (first and last 5 rows)
# print(df.to_string()) #prints everything


#selection by column: 
# print(df["Transaction ID"].to_string())

#selection by columns:
# print(df[["Transaction ID", "Date", "Description"]].to_string())

#Selection by row:
# print(df.loc[1])

# #selection by Name
df = pd.read_csv("data.csv", index_col = "Transaction ID")

# print(df.loc["TXN1000":"TXN1001", ["Description", "Amount"]])

# print(df.iloc[0:11:2, 0:3]) #every second row of first 11 rows + first three columns

# pokemon = input("Enter a pokemon name: ")

# try: 
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found ")

#DATA FILTERING: 
# desc = df[df["Coles"] >= 2]
# print(desc)


#categorise expenses: 
#Food: 
food_cat = df[df["Category"] == "Food"]

#transport:
transport_cat = df[df["Category"] == "Transport"]
#bills
bills_cat = df[df["Category"] == "Bills"]
#shopping
shopping_cat = df[df["Category"] == "Shopping"]




# # desc = df[(df["Description"] == "Coles") & (df["Category"] == "Food")]
# print(food_cat.to_string())

df['Date'] = pd.to_datetime(df['Date'])

# 2. Sort by the date column
df_sorted = df.sort_values(by='Date')
# print(df_sorted)

#calculate TOTAL spending: 
# print(df.sum(numeric_only =True))

#find biggest expenses: 
big_expenses = df[df["Amount"] >= 200]
# print(big_expenses)


group = df.groupby("Category")
#find means of Amount and group by category
print(group["Amount"].mean())

#maximum in each category 
print(group["Amount"].max())



