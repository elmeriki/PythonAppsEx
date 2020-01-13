from array import *

n = array('i',[])

user = int(input("Enter your array length ? "))

for i in range(user):

    x = int(input("Enter next value ? "))
    n.append(x)

print(n)