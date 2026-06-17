# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")
# print("Welcome")

# Функция привет
def sayHello():
    for i in range(100):
        print(i,"Привет")

# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()

# sayHello()
# sayHello()
# sayHello()

def greet(name):
    print("Привет", name)

# greet("Мадияр")
# greet("Диана")
# greet("Айгерим")
# greet("Аскар")



 
def show_user(name, age, address):
    print("Name:", name)
    print("Age:",age)
    print("Address:",address)
    
# show_user(19, "Ayan")
# show_user(19, "Ayan")
# show_user(19, "Ayan")
# show_user(19, "Ayan")
# show_user(19, "Ayan")
# show_user(19, "Ayan")
# show_user(19, "Ayan")

# print() return()

# def total1(a,b):
#     print(a + b)

# def total2(a,b):
#     print()
#     return a + b
    

# total1(4,5)
# print(total2(4,5))

# w1 = total1(1,2)
# w2 = total2(1,2)
# print(w1)
# print(w2)

# def ageCheck(age):
#     if age >= 18:
#         print("Checked")
#         return age
#     else:
#         print("Unchecked", age)
#         return age
        
# def uni(confirm):
#     if confirm > 18:
#         print("Принесите такие то доки")
#     else:
#         print("Вам еще рано в университет")

# alex = ageCheck(17) 
# uni(alex)   

# def avg(grades):
#     return sum(grades) / len(grades)

# student_grades = [90,81,87]

def clean_email(email):
    return email.strip().lower()


# email = "      STudent@gmail     "

# cleaned = clean_email(email)
# print(cleaned)

def is_valid_email(email):
    email = email.strip()

    if "@" in email and email.endswith(".com"):
        return True
    else:
        return False
    
print(is_valid_email("student@gmail.com"))
print(is_valid_email("student@gmail.kz"))