# When your data has different values, and even different measurement units, 
# it can be difficult to compare them.
# What is kilograms compared to meters? Or altitude compared to time?
# The answer to this problem is scaling. we can scale data into new values that are easier to compare.
# Take a look at the table below. it is the same data set that we used in the multiple regression chapter.
# but this time the volume column contains values in liters instead of cm3

# It can be difficult to compare the volume 1.0 with the weight 790.
# but if we scale them both into comparable values. we can easily see how much one value is compared to the other.
# There are different methods for scaling data, we will use a method called standardization.
# The standardization method uses this formula:
# z = (x - u) /s
# where 
# z is the new value
# x is original value
# u is the mean 
# s is the standard deviation
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("data/cars2.csv")

x = df[["Weight", "Volume"]]
y = df['CO2']

scaleX = scale.fit_transform(x)

regr = linear_model.LinearRegression()

regr .fit(scaleX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])


print(predictedCO2)