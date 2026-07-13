from abc import ABC, abstractmethod

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\nНачало операции: {func.__name__}")

        result = func(*args,**kwargs)

        print("Операция завершена.")

        return result
    return wrapper

class Product(ABC):
    def __init__(self,product_id, title,author,price):
        self.product_id = product_id
        self.title = title
        self.author = author
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            print("Ошибка цена долна быть больше нуля")
            return
        self.__price = new_price
    
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

class PaperBook(Product):
    def __init__(self,product_id,title,author,price,pages,quantity):
        super().__init__(product_id,title,author,price)
        self.pages = pages
        self.quantity = quantity
    
    def get_info(self):
        print(f"ID: {self.product_id}")
        print(f"Бумажная книга: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price} тенге")
        print(f"Количество страниц: {self.pages}")
        print(f"На складе: {self.quantity}")

    def is_available(self):
        return self.quantity > 0
    
    def buy(self):
        if not self.is_available():
            print("Книга={self.title} закончилась")
            return False
        self.quantity -= 1
        return True
    
# paper_book = PaperBook(
#     1,
#     "Python для начинающих",
#     "Иван Иванов",
#     6500,
#     350,
#     3
# )
# paper_book.get_info()
# print(paper_book.price)
# print(paper_book.buy())

# Id 2
# Название чистый код
# автор робер Мартин
# цена 10500
# страниц 500
# количество 2

class EBook(Product):
    def __init__(self,product_id,title,author,price,file_format,file_size):
        super().__init__(product_id,title,author,price)
        self.file_format = file_format
        self.file_size = file_size

    def get_info(self):
        print(f"ID: {self.product_id}")
        print(f"Электронная книга: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price} тенге")
        print(f"Формат файла: {self.file_format}")
        print(f"Размер файла: {self.file_size} МБ")

    def is_available(self):
        return True
    
    def buy(self):
        return True
    
paper_book = PaperBook(
    1,
    "Python для начинающих",
    "Алексей Иванов",
    6500,
    350,
    2
)
ebook = EBook(
    2,
    "Основы ООП",
    "Мария Петрова",
    3500,
    "PDF",
    12
)
products = [paper_book, ebook]
for product in products:
    product.get_info()
    print(product.is_available())
    print()

paper_book.buy()

for product in products:
    product.get_info()
    print(product.is_available())
    print()

