import sys

sys.setrecursionlimit(10)
# Recursion is calling a function from a function 
print(sys.getrecursionlimit())

def rec():
    print("Hello")
    rec()
    
rec()


# Recursion is a function calling it self 