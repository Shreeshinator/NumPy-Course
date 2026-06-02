import pandas as pd
# DataFrame is a 2D data structure, like a table with rows and columns
# It can hold different types of data (integers, strings, floats, etc.)
# Create a DataFrame from a dictionary
indices = []
for i in range(1, 4):
    indices.append("Emp." + str(i))

data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [25, 30, 35],
    'City': ['Bikini Bottom', 'Rock', 'Bikini Bottom']
}

df = pd.DataFrame(data, index=indices)

print(df)
print()
print(df.loc['Emp.2'])  # Access a row by index label
print() 

# Add a new column to the DataFrame
df['Salary'] = [50000, 45000, 55000]
print(df)
print()

new_row = pd.DataFrame({'Name': ['Sandy'], 'Age': [28], 'City': ['Bikini Bottom'], 'Salary': [60000]}, index=['Emp.4'])
df = pd.concat([df, new_row])
print(df)
print()
print(df['Salary'])  # Access a column by name