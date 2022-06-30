import pandas

df = pandas.read_csv("data/cars.csv")

X = df[['Weight', 'Volume']]
y = df["CO2"]

