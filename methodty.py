# Types of method

# Instace Method 
# Class Method 
# static method 

# an instance method is created inside the class to work with the object 
# instance method have two type  
# Accessor method (If you are using a method to only fetch the values )
# Mutator method (If you want to modilfy the values we will be using mutators)
# Class Method (If you want to make use of the class variable you will have to create a class method)
# if we are working with instance method we use self but if we are working with class method we use cls 
# static method (If you want a method which is not concern about class variable or instance variable 
# That will be refere to as static method)

class Student:
    
    school = "Pine Valley Institute"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getSchoolName(cls):
        return(cls.school)
    
    @classmethod
    def changeSchoolName(cls):
        cls.school = "New Pine Valley Institute"
        return(cls.school)
    
    @staticmethod
    def greetingMessage():
        print("You are welcome to Pine Valley Institute")
        
    
    
s1= Student(10,30,13)
print(s1.avg())
print(Student.getSchoolName())
print(Student.changeSchoolName())
Student.greetingMessage()

    
    
