from abc import ABC, abstractmethod

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\nНачало операции: {func.__name__}")
        result = func(*args, **kwargs)
        print("Операция завершена.")
        return result
    return wrapper

class Product(ABC):
    def __init__(self, product_id, title, author, price):
        self.product_id = product_id
        self.title = title
        self.author = author
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: цена должна быть больше нуля")
            return
        self.__price = new_price
    
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

class PaperBook(Product):
    def __init__(self, product_id, title, author, price, pages, quantity):
        super().__init__(product_id, title, author, price)
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
            print(f"Книга {self.title} закончилась")  # Исправлено: добавлен f-строка
            return False
        self.quantity -= 1
        return True

class EBook(Product):
    def __init__(self, product_id, title, author, price, file_format, file_size):
        super().__init__(product_id, title, author, price)
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

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    @log_action
    def add_product(self, product):
        self.products.append(product)
        print(f"Товар {product.title} добавлен в магазин")

    def show_catalog(self):
        if len(self.products) == 0:
            print("Каталог магазина пуст")
            return
        
        print(f"\n======= КАТАЛОГ: {self.name} =======")
        for product in self.products:
            product.get_info()
            print("-" * 30)
        
    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

class Cart:
    def __init__(self):
        self.items = []

    @log_action
    def add_product(self, product):
        if not product.is_available():
            print(f"Товара {product.title} нет в наличии")
            return
        self.items.append(product)
        print(f"Товар {product.title} добавлен в корзину")

    def show_cart(self):
        if len(self.items) == 0:
            print("Корзина пуста")
            return
        print("\n======= КОРЗИНА =======")
        for index, product in enumerate(self.items, start=1):
            print(f"{index}. {product.title} - {product.price} тенге")
        # Исправлено: вывод итоговой суммы перенесен ЗА пределы цикла
        print(f"Итого: {self.get_total_price()} тенге")
    
    def get_total_price(self):
        total = 0
        for product in self.items:
            total += product.price
        return total  # Исправлено: return перенесен ЗА пределы цикла `for`
    
    @log_action
    def checkout(self):
        if len(self.items) == 0:
            print("Невозможно оформить пустой заказ")
            return

        purchased_products = []

        for product in self.items:
            if product.buy():
                purchased_products.append(product)
            else:
                print(f"Не удалось купить {product.title}")
            
        if len(purchased_products) == 0:
            print("Не удалось купить ни одного продукта")
            return
        
        # Исправлено: Вся логика успешного вывода переписана без лишних повторений
        print("\nЗаказ успешно оформлен!")
        print("Купленные товары:")
        total = 0 
        for product in purchased_products:
            total += product.price
            print(f" - {product.title}: {product.price} тенге")
            
        print(f"Итоговая сумма: {total} тенге")
        self.items.clear()

# --- Инициализация и запуск ---
store = Store("Book world")

# Добавим несколько книг для демонстрации
book1 = PaperBook(1, "Python", "Aleksei", 6500, 350, 1)
book2 = PaperBook(2, "Java", "Alex", 8500, 1000, 2)
ebook = EBook(3, "Basic OOP", "Mariya", 4000, "PDF", 12)

store.add_product(book1)
store.add_product(book2)
store.add_product(ebook)

cart = Cart()

while True:
    print("\n=== ЭЛЕКТРОННЫЙ МАГАЗИН КНИГ ===")
    print("1. Показать каталог")
    print("2. Добавить товар в корзину")
    print("3. Показать корзину")
    print("4. Оформить заказ")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        store.show_catalog()
    elif choice == "2":
        try:
            product_id = int(input("Введите ID товара: "))
        except ValueError:
            print("Ошибка: необходимо ввести число.")
            continue

        product = store.find_product_by_id(product_id)
        if product is None:
            print("Товар с таким ID не найден")
        else:
            cart.add_product(product)
    
    elif choice == "3":
        cart.show_cart()
    elif choice == "4":
        cart.checkout()
    elif choice == "0":
        print("Спасибо за использование магазина!")
        break
    else:
        print("Такого пункта меню нет.")