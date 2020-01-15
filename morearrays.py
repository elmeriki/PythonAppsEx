from array import *

arr = array('i',[])

n =int(input("Enter the length of array? "))

for i in range(n):
    x = int(input("Enter next Value? "))
    arr.append(x)
    
print(arr)
    
val = int(input("What is the Value you want to search? "))    
# k=0
# for e in arr:
#     if e ==val:
#         print("The index position is ", k) 
#         break
#     k=k+1
print(arr.index(val))



