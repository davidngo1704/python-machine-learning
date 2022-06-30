#Standard Deviation
# is a number describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A hight standard deviation means that the values are spread out over a wider value.
import numpy
speed = [86,87,88,86,87,85,86]

print(numpy.std(speed))

# Variance:
# Varience is another number that indicates how spread out the values are.
# In fact, if you take the square root of the variance, you get the  standard deviation.
# Or the other way around, if you multiply the standard deviation by ifself, you get the variance.
print(numpy.var(speed))