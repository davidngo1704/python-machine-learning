# Regression
# The term regression is used when you try to find the relationship between variables.
# In machine learning, and in statistical modeling. that relationship is used to predict the outcome of future events.
# Linear Regession uses the relationship between the data-points to draw a straight line through all them.
# This line can be used to predict future values.
# In machine learning, predicting the future is very impotant.

import matplotlib.pyplot as plt
from scipy import stats


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r)
def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# R for relationship 
# it is important to know the relationship between the values of the x-axis and the values of the y-axis
# if there are no relationship the linear regression can't be used to predict anything.

# This relationship - the coefficient of correlation - is called r.
# The r value ranges from -1 to 1. where 0 means no relationship.
# and 1(and -1) means 100% related.
# The result -0.76 shows that there is a relationship. not perfect. but it indicates that we could use 
# linear regression in future predictions.

# Predict future values
