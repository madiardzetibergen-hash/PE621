def add(a: int, b: int) -> int:
    """Функция складывает два числа"""
    return a + b

add.description = "Складывает два числа"
add.version ="1.0"

print(add.__name__)
print(add.__doc__)
print(add.__annotations__)
print()
print(add.description)
print(add.version)

def add2(a, b):
    return a + b


print(add2("qwerty", "qwerty"))


# ===============НОВАЯ ТЕМА================
def outer():
    print("Это внешняя функция")
    
    def inner():
        print("Это внутренняя функция")
    
    inner()

# outer()

def create_student_report(name,scores):
    def calculate_average():
        return sum(scores) / len(scores)
    
    def status_scholarship(average):
        if average >= 70:
            return "Save"
        return "Unsave"
    
    average = calculate_average()
    status = status_scholarship(average)

    return f"Студент: {name}, средний балл: {average}, статус: {status}"

# report = create_student_report("Али", [80,77,90,91,68])
# print(report)

# count = 0

# print(count)
# def increase():
#     global count
#     count = count + 1

# increase()
# increase()
# increase()

# print(count)

# Это правильно
# def outer():
#     count = 0

#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
    
#     inner()
#     inner()
#     inner()

# outer()

# Это ошибка

# count = 0

# def outer():
   

#     def inner():
#         global count
#         count += 1
#         print(count)
    
#     inner()

# outer()



# def add(*numbers):
#     print(numbers)

# add("qwerty", "qwerty","qwerty","qwerty",123,123,False)

# def show_user(**kwargs):
#     print(kwargs)

# show_user(name = "ALi", age=18, city="Almaty")

# def create_user(**user):
#     if "name" not in user:
#         return "Ошибка: имя обязательно"
    
#     if "age" not in user:
#         return "Ошибка: возраст обязателен"
    
#     return f"Пользователь {user['name']} создан"

# print(create_user(name = "ALi", age = 18))
# print(create_user(name = "Mansur"))

def create_order(username, *products, delivery = False, **details):
    print(f"Покупатель: {username}")
    print(f"Товары:")
    for i in products:
        print(f"- {i}")
    
    print(f"Доставка: {delivery}")
    print("Дополнительная информация:")
    for key,value in details.items():
        print(f"{key} : {value}")

create_order("Али", "Ноутбук", "Мышка","Клавиатура", delivery=True, city="Алматы", payment ="Kaspi alakan 🖐")

