# how to use a class variable 

class Product:
    
    vat ="15%"
    
    def __init__(self):
        print("Hello World")
        
    def main(self):
        print(self.vat)
        
Product.vat=999   
fruit = Product()

        
        
    
        
    
