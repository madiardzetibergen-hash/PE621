# age = int(input("Введите ваш возраст: "))
# print(f"Через год вам будет {age + 1}")

# try:
#     age = int(input("Введите ваш возраст: "))
#     print(f"Через год вам будет {age + 1}")
# except ValueError:
#     print("Ошибка: необходимо ввести число")
# finally:
#     print("Программа завершила свою работу")

# try:
#     first_number = int(input("Введите ваше первое число: "))
#     second_number = int(input("Введите ваше второе число: "))

#     result = first_number / second_number
#     print("Результат: ", result)
# except ValueError:
#     print("Ошибка нужно вводить только числа")
# except ZeroDivisionError:
#     print("Ошибка: на ноль делить нельзя")

# try:
#     first_number = int(input("Введите ваше первое число: "))
#     second_number = int(input("Введите ваше второе число: "))

#     result = first_number / second_number
#     print("Результат: ", result)
# except (ValueError,ZeroDivisionError):
#     print("Вы ввели неправильные данные")

# try:
#     number = int(input("Введите число: "))
# except ValueError as error:
#     print("Произошла ошибка", error)

# try:
#     first_number = int(input("Введите ваше первое число: "))
#     second_number = int(input("Введите ваше второе число: "))

#     result = first_number / second_number
#     print("Результат: ", result)
# except ZeroDivisionError as error:
#     print("Какая то ошибка", error)

# try:
#     number = int(input("Введите число: "))
    
#     result  = 10 / number
#     print("Ваш ответ", result)

# except Exception as error:
#     print("Произошла ошибка: ",error)


# raise 
# try:
#     age = int(input("Введите возраст: "))
    
#     if age < 0:
#         print("Возраст не может быть отрицательным")
#     else:
#         print("Возраст:", age)

# except ValueError:
#     print("Ошибка: Введите числовое значение")

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
    
#     def withdraw(self,amount):
#         if amount < 0:
#             raise ValueError("Сумма должна быть больше нуля")
#         if amount > self.balance:
#             raise ValueError("Недостаточно средств")
        
#         self.balance -= amount
#         print(f"Снято: {amount}" )
#         print(f"Остаток: {self.balance}")

# account = BankAccount("Алексей",10000)

# try:
#     amount = int(input("Введите сумму снятия: "))
#     account.withdraw(amount)

# except ValueError as error:
#     print("Операция отклонена:", error)

# Практика -> решение
# 1
# try:
#     number = int(input("Введите целое число: "))
#     print("Квадрат числа:", number ** 2)

# except ValueError:
#     print("Ошибка необходимо ввести целое число")

# 2
# try:
#     first_number = int(input("Введите ваше первое число: "))
#     second_number = int(input("Введите ваше второе число: "))

#     result = first_number / second_number
#     print("Результат: ", result)
# except ZeroDivisionError as error:
#     print("Какая то ошибка", error)

# 3.
# fruits = ["яблоко", "банан", "апельсин", "груша"]

# try:
#     index = int(input("Введите индекс: "))
#     print("Выбранный фрукт: ", fruits[index])

# except ValueError:
#     print("Ошибка: индекс необходимо ввести целым числом")
# except IndexError:
#     print("Ошибка: элемента с таким индексом нет")

# 4
# student = {
#     "name": "Алина",
#     "age": 17,
#     "group": "Python-1"
# }
# try:
#     key = int(input("Введите ключ элемента: "))
#     print("Значение:", student[key])

# except KeyError:
#     print("Ошибка: такого ключа нет")

# 5.

# while True:
#     try:
#         age = int(input("Введите возраст: "))
#         print("Возраст успешно сохранен", age)
#         break
#     except ValueError:
#         print("Ошибка: возраст нужно вводить целым числом")

# 6.
# try:
#     first_number = float(input("Введите ваше первое число: "))
#     operation = input("Введите операцию (+,-,*,/): ")
#     second_number = float(input("Введите ваше второе число: "))

#     if operation == "+":
#         result = first_number + second_number
#         print("Ваш ответ", result)
#     elif operation == "-":
#         result = first_number - second_number        
#         print("Ваш ответ", result)
#     elif operation == "*":
#         result = first_number * second_number
#         print("Ваш ответ", result)
#     elif operation == "/":
#         result = first_number / second_number
#         print("Ваш ответ", result)
#     else:
#         result = None
#         print("Неизвестная ошибка")
    
# except ValueError:
#     print("Ошибка: нужно вводить только числа")
# except ZeroDivisionError:
#     print("Ошибка: на ноль делить нельзя")
# finally:
#     print("Работа калькулятора завершена")

# 7.
# try:
#     age = int(input("Введите возраст: "))

#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным")
    
#     if age > 120:
#         raise ValueError("Возвраст не может быть больше 120")
    
#     if age < 16:
#         raise ValueError("Доступ разрещен с 16 лет")
    
#     else:
#         print("Вход разрешен")

# except ValueError as error:
#     print("Ошибка: ", error)

# ===============2 пара========= Асинхрон
# print("Шаг1")
# print("Шаг2")
# print("Шаг3")

# import time

# def download_file(file_name):
#     print(f"Начинаем скачавание {file_name}")

#     time.sleep(3)
#     print(f"Файл {file_name} скачан")

# download_file("image.png")
# download_file("music.mp3")
# download_file("document.word")

# async def hello():
#     print("Привет")
# корутины

import asyncio

# async def hello():
#     print("Привет из асинхронной функции")

# asyncio.run(hello())

# async def show_message():
#     print("Начало")

#     await asyncio.sleep(3)
#     print('Конец')

    

# asyncio.run(show_message())

# async def download_file(file_name):
#     print(f"Начинаем скачивание: {file_name}")

#     await asyncio.sleep(3)
#     print(f"Файл скачан:{file_name}")

# async def main():
#     await download_file("photo.png")

#     await download_file("video.mp4")

#     await download_file("document.pdf")

# asyncio.run(main())
