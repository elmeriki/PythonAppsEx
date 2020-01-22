# # A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a, b: a * b
# print(x(5, 6))

# How to use filter function with lamda 

# Filter function takes two arguement(function and alteration)
# Maps function takes two arguement (The function and sequence )

nums= [2,3,5,7,8,9,12,5,36,42]
even = list(filter(lambda a : a%2==0,nums))

double = list(map(lambda n : n*2,nums))

print(even)

print(double)
