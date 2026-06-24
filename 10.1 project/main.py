from products import show_products, search_product_by_name
from cart import add_to_cart, show_cart,check_the_order
from utils import input_number,print_line

def show_menu():
    print("===== МАГАЗИН =====")
    print("1. Показать товары")
    print("2. Найти товар")
    print("3. Добавить товар в корзину")
    print("4. Показать корзину")
    print("5. Проверить заказ")
    print("0. Выйти")

def main():
    while True:
        show_menu()

        choice = input("Выберите действие")
        if choice == "1":
            show_products()
        elif choice == "2":
            query = input("Введите название товара: ")
            results = search_product_by_name(query)

            if len(results) == 0:
                print("Ничего не найдено")
            else:
                print("===== Результат поиска =====")
                for product in results:
                    print(
                        f"{product["id"]} | "
                        f"{product["name"]} | "
                        f"{product["price"]} тг | "
                        f"{product["category"]}"
                    )
        elif choice == "3":
            product_id = input_number("Введите id товара: ")
            quantity = input_number("Введите количество: ")
            add_to_cart(product_id, quantity)
        elif choice == "4":
            show_cart()
        elif choice == "5":
            check_the_order()
        elif choice == "0":
            print("Программа завершена")
            break
        else:
            print("Ошибка: такого пункта нет")
            print_line

if __name__ == "__main__":
    main()