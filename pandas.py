import pandas as pd

# Example: Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Getting a statistical description of the data
print(df.describe())

