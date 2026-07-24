# Повторение
# day = input("Введите день недели: ")
# if day == "1" or day == "Пн":
#     print("Пн")
# elif day == "2" or day == "Вт":
#     print("Вт")
# elif day == "3" or day == "Ср":
#     print("Ср")
# elif day == "4" or day == "Чт":
#     print("Чт")
# elif day == "5" or day == "Пт":
#     print("Пт")
# elif day == "6" or day == "Сб":
#     print("Сб")
# elif day == "7" or day == "Вс":
#     print("Вс")
# else:
#     print("Введите день недели")

# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# if login == "admin" and password == "123":
#     print("1")
# elif login != "admin":
#     print("Неправильный логин")
# else:
#     print("0")


# Циклы
# 1)
# i = 0
# while i <= 3:
#     print(i)
#     i += 2
# 2)
# i = 10
# while i >= 1:
#     print(i, "Привет")
#     i -= 1
# 3)
# i = 2
# while i <= 20:
#     print(i)
#     i += 2

# 3.2)
# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 1
# total = 0
# while i <= 5:
#     total = total + i
#     i += 1
# print("Сумма", total)

# password  = ""
# while password != "1234":
#     password = input("Введите пароль: ")
# print("Доступ разрещен")

# attempt = 1
# password  = input("Введите пароль: ")
# while password != "1234":
#     if attempt == 3:
#         print("Доступ запрещен")
#         break
#     print("Попытка: ", attempt)
#     password = input("Введите пароль: ")
#     attempt += 1
# else:
#     print("Доступ разрещен")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# i = 10
# while i >= 1:
#     print(i, "Привет")
#     i -= 1

# i = 1
# while i <= 100:
#     print(i)
#     i += 2

# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# n = int(input("Введите число: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

# n = int(input("Введите число: "))
# i = 1
# total = 0
# while i <= n:
#     print(i)
#     i += 1
#     total = total + i
# print("Сумму", total)

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,n,2):
#     print(i)

# for i in range(1,101):
#     if i % 2 == 1:
#         print(i)

# count = 0
# word = input("Введите слово")
# for i in word:
#     count = count + 1
#     print(i)
# print("Quantity: ", count)

# total = 0
# total2 = 0
# for i in range(1,101):
#     total = total + i
#     if i % 2 == 1:
#         total2 = total2 + i
#         print(i)
# print(total, total2)