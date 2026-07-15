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

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Сумма должна быть больше нуля")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        
        self.balance -= amount
        print(f"Снято: {amount}" )
        print(f"Остаток: {self.balance}")

account = BankAccount("Алексей",10000)

try:
    amount = int(input("Введите сумму снятия: "))
    account.withdraw(amount)

except ValueError as error:
    print("Операция отклонена:", error)

