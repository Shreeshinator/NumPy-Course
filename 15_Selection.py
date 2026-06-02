import pandas as pd

indices = []
for i in range(1, 4):
    indices.append("Emp." + str(i))

data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [25, 30, 35],
    'City': ['Bikini Bottom', 'Rock', 'Bikini Bottom']
}

df = pd.DataFrame(data, index=indices)
# Selection in DataFrames
# Accessing a single column
print(df['Name'])  # Access the 'Name' column
print()
# Accessing multiple columns
print(df[['Name', 'City']])  # Access the 'Name' and 'City' columns
print()
# Accessing rows using .loc

print(df.loc['Emp.1'])  # Access the row with index 'Emp.1'
print()
print(df.loc['Emp.1', 'Name'])  # Access the 'Name' of the row with index 'Emp.1'
print()