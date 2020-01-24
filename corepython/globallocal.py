# GLOBAL AND LOCAL VARIABLES (SCOPE)

x = 10
def scopem(a,b):
    globals()['x']
    a = a + b
    print(a)
    
print(x)   
scopem(x,90)

