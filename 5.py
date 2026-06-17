# for i in range(3):
#     for j in range(2):
#         print(i,j)

# for i in range(3):
#     print("Внешний цикл", i)
    
#     for j in range(9):
#         print("Внутренний цикл", j)

# for i in range(1,6):
#     for j in range(1,6):
#         print("i= ", i, "j= ", j, "Ответ= ", i * j,end = "\t")
    
#     print()

# for i in range(5):
#     # print("*", end=" ")
#     for j in range(5):
#         print("*", end=" ")
#     print("*")

# students = ["Ali", "Mansur", "Dana"]
# students[0] = "Arman"
# print("Ali" in students)
# print("Dana" in students)
# students.append("Qwerty")
# print(students)
# print(len(students))

# students = ["Ali", "Mansur", "Dana"]
# for i in students:
#     print(len(i))

# students = ["Ali", "Mansur", "Dana"]
# for i in range(len(students)):
#     print(i, students[i])
# for index, student in enumerate(students, start=1):
#     print(index,student)

# nums = [10,20,30,40,50,60]
# print(nums[:3])
# print(nums[::2])
# print(nums[3:0])
# print(nums[::-1])

# students = ["Ali", "Mansur"]
# new_students = ["Dias", "Miras"]
# students.extend(new_students)
# students.remove("A")
# students.pop(-2)
# students.append("Qwerty")
# students.insert(1, "Asd")
# students.extend("Qwerty", "Asd")
# students.clear()
# print(students.count(1))
# print(students)
# students.reverse()
# print(students)

# numbers = [5,2,4,3,7,8,0]
# names = ["Ян", "Алмас", "Жанниет", "Alex", "Harry"]
# names.sort()
# print(names)
# numbers.sort()
# numbers.sort(reverse=False)
# print(numbers)

# numbers = [1,2,3]
# new_numbers = numbers.copy()
# new_numbers.append(4)
# print(numbers)
# print(new_numbers)

# numbers = [1,2,3]
# numbers.append()
# print(numbers)

# print(numbers.index(2))

# students = (1,2,3,4,5)
# print(students[0])
# students[::-1]
# print(students)

# word = "Hello"
# print("e" in word)
# print(word)

# lower() 
# word = "HELLO WORLD"
# print(word.lower())
# upper()
# word = "hello world"
# print(word.upper())
# title()
# word = "hello world"
# print(word.title())
# word = "hello world"
# print(word.capitalize())

export # strip(), lstrip(), rstrip()
# text = "        hello         "
# print(text.strip())

# replace()

# text = "I like Golang"

# new_text = text.replace("Golang", "Rust")
# print(new_text)

# find()

# word = "Hello people people python"
# print(word.count("people"))

# word = "Python lesson"
# print(word.startswith("lesson"))
# print(word.endswith("lesson"))

# split()
# text = "12 3"
# names = text.split()
# print(names) 

# join()
# words = ["Python", "is", "cool"]

# text = " ".join(words) 
# print(text)

# isdigit
# text = ""
# print(text.isdigit())

# isaplha
# text = "qwet123as123"
# print(text.isalpha())

# isalnum
# text = "$"
# print(text.isalnum())

