# grades = [70,80,85,95,100]

# total = sum(grades)
# average = total / len(grades)
# max_grade = max(grades)
# min_grade = min(grades)

# print("Все показать каждый элемент")


# numbers = [1,4,7,10,13,16,20]

# even_numbers = []

# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

# product = ("Laptop", 350000,3)

# name,price,count = product
# print("Title", name)
# print("price",price)
# print("count",count)
# print("Sum: " , price * count)

# student ={ 
#     "name": "Dana",
#     "age":20,
#     "grade":84
# }

# print(student["name"])
# print(student["age"])
# print(student["grade"])

# if student["grade"] >= 70:
#     print("Студент прошел курс")
# else:
#     print("Студент не прошел курс")


# languages = ["Python", "Java", "Python", "C++", "Java", "GO"]

# unique_lang = set(languages)
# print(languages)
# print(unique_lang)

# text = "I am learning Python programming"

# text = text.lower()

# if "python" in text:
#     print("Слово python есть")
# else:
#     print("слово python нет")
# lower()
# upper()
# title
# strip()
# replace()
# split()
# ("")join


# email = input("Введите почту")

# email = email.strip()

# if "@" in email and email.endswith(".com"):
#     print("Email корректный")
# else:
#     print("некорректный")

# students = [
#     {
#         "id":1,
#         "name":"Qwerty",
#         "grade": [98,95,89,91,99],
#         "skills": {"python", "html","css"}
#     },
#     {
#         "id":2,
#         "name":"Asd",
#         "grade":88
#     }
# ]

# Сложные структуры данных

# student = {
#     "name": "Ayan",
#     "grades": [15,16,17,18,19,20]
# }
# print(student["grades"][1])

# students = [
#     {"name":"Ayan", "grade":80},
#     {"name":"Dana", "grade":112},
#     {"name":"Artem", "grade":77},
# ]
# print(students[0]["grade"])

users ={
    1: {
        "name": "Ayan",
        "grade": 78
    },
    2: {
        "name": "Dana",
        "grade":{"grades":[88,99,11,22]}
    }
}
# print(users[2]["name"])
# print(users[2]["grade"]["grades"][3])

user = {
    "name": "Ayan",
    "skills": {"python", "html", "go", "hono"}
}
# print(user["skills"])
# for i in user["skills"]:
#     if i == "hono":
#         print(i)

# points = [
#     0(10,20),
#     1(30,40),
#     2(50,60)
# ]
# print(points[0][0])

# cart = [
#     {
#         "name": "Phone",
#         "price": 1234123,
#         "count": 1
#     },
#        {
#         "name": "Phone",
#         "price": 1234123,
#         "count": 1
#     },
# ]

# course = {
#     "title": "Python Basic",
#     "students":[
#         {
#             "name": "Talipzhan",
#             "progress": 80,
#             "completed_lesson": ["var", "if else", "while/for"]
#         },
#         {
#             "name": "Talipzhan",
#             "progress": 80,
#             "completed_lesson": ["var", "if else", "while/for"]
#         }
#     ]
# }