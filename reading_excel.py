import pandas as pd

data = pd.read_excel("./data/transactions.xlsx")

df = pd.DataFrame(data)

print(df.head(3))