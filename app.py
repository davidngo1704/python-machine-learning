import pandas as pd

data = pd.read_json("data/data.json")

print(data.to_string())