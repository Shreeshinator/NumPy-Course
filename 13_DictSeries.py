import pandas as pd

calories = {"Day1":1750, "Day2": 2110, "Day3": 1790}
series = pd.Series(calories)

print(series)
print()
print(series["Day2"]) # Accessing a specific value using the index label