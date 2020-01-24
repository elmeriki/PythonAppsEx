from numpy import *
from numpy.core._multiarray_umath import concatenate
from array import array

# More solution on creating arrays in python 

# arr = array([1,2,3,4,5])
# arr = arr + 6
# print(arr)

# arr1 = array([1,2,3,4,5])
# arr2 = array([1,3,9,9,5])
# arr3 = arr1 + arr2
# print(arr3)

# How to add one array to another Array

arr1 = array([1,2,3,4,5])
arr2 = array([1,3,9,9,5])
print(concatenate([arr1,arr2]))

# This is how to concatenate one array to another array 
