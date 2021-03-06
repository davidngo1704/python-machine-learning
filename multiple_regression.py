import pandas

from sklearn import linear_model

df = pandas.read_csv("data/cars.csv")

x = df[['Weight', 'Volume']]
y = df["CO2"]

regr = linear_model.LinearRegression()

regr.fit(x, y)

print(regr.coef_)

predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

# Coefficient
# The coefficient is a factor that describes the relationship with an unknown variable.
