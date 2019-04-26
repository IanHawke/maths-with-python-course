import math

# 8! written out by hand
eight_factorial = 8*7*6*5*4*3*2*1

# Print the result
print(eight_factorial)

# print the result from the math library
print(math.factorial(8))

# Print that the two agree
print(eight_factorial == math.factorial(8))
