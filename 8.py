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

# def clean_email(email):
#     return email.strip().lower()


# email = "      STudent@gmail     "

# cleaned = clean_email(email)
# print(cleaned)

# def is_valid_email(email):
#     email = email.strip()

#     if "@" in email and email.endswith(".com"):
#         return True
#     else:
#         return False
    
# print(is_valid_email("student@gmail.com"))
# print(is_valid_email("student@gmail.kz"))


def get_total(numbers):
    return sum(numbers)

# print(get_total([1,2,3,4,5]))

def get_positive_numbers(numbers):
    positive = []
    negative = []
    neutral = []

    for i in numbers:
        if i > 0:
            
            positive.append(i)
        elif i < 0:
            
            negative.append(i)
        else:
            
            neutral.append(i)
    print("Положительные", positive)
    print("Отрицательные", negative)
    print("Нейтральные", neutral)
    return positive, negative, neutral

# numbers = [-3,5,-10,0,-4,1,2]

# get_positive_numbers(numbers)

# def show_student(student):
#     print("Имя", student["name"])
#     print("Возраст", student["age"])
#     print("Группа", student["group"])

# student = {
#     "name": "Askar",
#     "age": 21,
#     "group": "PA-441"
# }
# show_student(student)

# def create_user(name,age,email):
#     user = {
#         "name": name,
#         "age": age,
#         "email": email
#     }
#     return user

# new_user = create_user("Ayan", 18, "ayan@gmail.com")

# print(new_user)

# Функция ищет студента с лучшей оценкой

def get_best_student(students):
    best_student = students[0]

    for i in students:
        if i["grade"] > best_student["grade"]:
            best_student = i
    return best_student

students= [
    {
    "name": "Askar",
    "grade": 80,
    "group": "PA-441"
    },
      {
    "name": "Askar2",
    "grade": 85,
    "group": "PA-441"
    },
      {
    "name": "Askar3",
    "grade": 63,
    "group": "PA-441"
    },
      {
    "name": "Askar4",
    "grade": 99,
    "group": "PA-441"
    },
      {
    "name": "Askar5",
    "grade": 100,
    "group": "PA-441"
    },
]

best = get_best_student(students)
print(best)