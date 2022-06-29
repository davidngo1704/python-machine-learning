import pandas as pd

data = pd.read_json("data/data.json")

print(data.head(3))