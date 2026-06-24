from products import find_product_by_id
cart = {}
# 1. Функция добавления товара в корзину
def add_to_cart(product_id, quantity):
    product = find_product_by_id(product_id)

    if product is None:
        print("Товар не найден")
        return
    
    if quantity <= 0:
        print("Количество должно быть больше 0")
        return
    
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    print(f"Товар {product["name"]} добавлен в корзину")

# 2. Функция показа корзины
def show_cart():
    if len(cart) == 0:
        print("Корзина пустая")
        return
    
    print("===== ВАША КОРЗИНА =====")

    total = 0

    for product_id, quanity in cart.items():
        product = find_product_by_id(product_id)
        item_total = product["price"] * quanity

        print(
            f"{product["name"]} | "
            f"{quanity} шт | "
            f"{item_total} тг"
        )
    print(f"Итого: {total} тг")