class Product:
    def __init__(self,id,name,price,category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.grades = []
    
    def show_info(self):
        print(f"{self.id}, {self.name}, {self.price}, {self.category}")
    
    def add_grades(self,grade):





product1 = Product(1,"Laptop", "2345678", "Tech")
product2 = Product(2,"Laptop2", "2345678", "Tech")
product2.show_info()
product1.show_info()
print(product1.name)

sum
