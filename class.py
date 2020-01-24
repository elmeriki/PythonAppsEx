# Class is the Design of an object and an objcet is the copy
# of the class or an instance of ZipFile 
# The class for reading and writing ZIP files.  See section 

# class Person:    
    
#     def message(self):
#         print("Hello")
        
        
# per = Person()    
# per.message()
# Person.message(per)

class Car:
    
    def __init__(self,name,year):
        self.name=name
        self.year=year
        
    def driving(self):
        print(self.name,self.year)
        
car1 = Car("Polo",2020)
car1.driving()



