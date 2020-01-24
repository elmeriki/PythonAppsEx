# if you pass a value to a function either by value or 
# by reference they dont share the same addres or storage address  

# def delete(y):
#     x=y +10 
#     return x

# xy = 10
# print(delete(xy))

# TYPES OF ARGUEMENT 

# Keyword
# Position
# Default and 
# variable length 

# The variable we supply in the round bracket of our function is call formal arquement 
# and when we are invoking the function and the value we pass is call the actual arguement
 
# def add(x,y):  
    
#     c = x + y
#     print(c)
    
# add(10,10)


# def person(name,age):
#     print(name)
#     print(age)
    
# person(age=80,name="Solomon")

# we have pass the values by keword 
# def person(name,age=10):
#     print(name)
#     print(age)
    
# person("Meriki")

# if no value is pass in the place of age the default value will be implemented 

# Variable length 

# This can allow multiple valus to be printed using the arguement type variable length 

# def sum(a,*b):
#     c = a
#     for i in b:
#         c =c+i
#     print(c)
 
   
# sum(90,90,90,90)

def person(name,**data):
    print(name)
    print(data)

person(name="meriki",age=90,city="Pretoria")

