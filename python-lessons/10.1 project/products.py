products = [
    {
        "id":1,
        "name":"Ноутбук Lenovo",
        "price": 400000,
        "category": "Техника"
    },
    {
        "id":2,
        "name":"Iphone 13",
        "price": 300000,
        "category": "Техника"
    },
    {
        "id":3,
        "name":"Наушники JBL",
        "price": 25000,
        "category": "Аксессуары"
    },
    {
        "id":4,
        "name":"Клавиатура Logitech",
        "price": 30000,
        "category": "Аксессуары"
    },
    {
        "id":5,
        "name":"Футболка XL",
        "price": 10000,
        "category": "Одежда"
    }
]

# 1. Функция показа всех товаров
def show_products():
    print("===== КАТАЛОГ ТОВАРОВ =====")
    for product in products:
        print(
            f"{product['id']}. {product["name"]} | "
            f"{product["price"]} тг | "
            f"{product["category"]}"
        )

# 2. Функция поиска товаров по name
def search_product_by_name(query):
    results = []
    for product in products:
        if query.strip().lower() in product["name"].lower():
            results.append(product)
    return results

# 3. Функция поиска товаров по id
def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None