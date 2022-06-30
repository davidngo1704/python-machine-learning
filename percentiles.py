# Percentiles are used in statistics to give you a number that
# describes the value that a given percent of the values are lower than.
# Example: Let's say we have an array of the ages of all the people that lives in a street.

import numpy

ages = [5,31,43,48]

print(numpy.percentile(ages, 75))

# 75% of the people are 43 or younger.

