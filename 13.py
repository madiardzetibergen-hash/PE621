# =============== ПОВТОРЕНИЕ ===================

# class CourseRoom():
#     def __init__(self,title,limit):
#         self.title = title
#         self.limit = limit
#         self.__students = []

#     def add_student(self,name):
#         if len(self.__students) >= self.limit:
#             print(f"В группе {self.title} уже нет мест")
#             return
    
#         self.__students.append(name)
#         print(f"{name} добавлен в группу {self.title}")
    
#     def remove_student(self,name):
#         if name in self.__students:
#             self.__students.remove(name)
#             print(f"{name} удален из группы")
#         else:
#             print(f"{name} не найден в группе")
    
#     def show_info(self):
#         print(f"Курс: {self.title}")
#         print(f"Лимит: {self.limit}")
#         print(f"Студентов сейчас: {len(self.__students)}")
#         print(f"Список студентов: {self.__students}")
    
#     def get_students_count(self):
#         return len(self.__students)

# python_group = CourseRoom("Python OOP", 3)
# python_group.add_student("Диас")
# python_group.add_student("Мансур")
# python_group.add_student("Дана")
# python_group.add_student("Магжан")
# python_group.show_info()
# print(python_group.get_students_count())


# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

#     def login(self):
#         print(f"{self.name} вошел в систему")

# class Student(User):
#     def __init__(self,name,email,group):
#         super().__init__(name,email)
#         self.group = group
    
#     def send_homework(self):
#         print(f"{self.name} отправил домашнее задание")

# class Teacher(User):
#     def __init__(self,name,email,subject):
#         super().__init__(name,email)
    
#         self.subject = subject

#     def check_homework(self):
#         print(f"{self.name} проверяет домашние задание по предмету {self.subject}")

# student = Student("Alex", "alex@gmail.com","Python-1")
# teacher = Teacher("Artem", "artem@gmail.com", "Python")

# student.login()
# student.send_homework()

# teacher.login()
# teacher.check_homework()



# =============== НОВАЯ ТЕМА ===================
# Абстракция - это когда мы описываем что обьект должен уметь, но не 
# расписываем сразу как именно он это делает

from abc import ABC, abstractmethod

# class AssigmentChecker(ABC):
#     def __init__(self,title):
#         self.title = title
    
#     @abstractmethod
#     def check(self,solution):
#         pass
    
#     def show_start_message(self):
#         pass

# class PythonChecker(AssigmentChecker):
#     def check(self,solution):

#         if "def" in solution and "return" in solution:
#             return "Python-задание принято"
#         return "Python-задание нужно доработать"

# class SQLChecker(AssigmentChecker):
#     def check(self,solution):
#         upper_solution = solution.upper()

#         if "SELECT" in upper_solution and "FROM" in upper_solution:
#             return "SQL-задание принято"
#         return "SQL-задание нужно доработать"

# class ReactChecker(AssigmentChecker):
#     def check(self,solution):
#         if "useState" in solution or "useEffect" in solution:
#             return "React-задание принято"
#         return "React-задание нужно доработать"

# class JavaChecker(AssigmentChecker):
#     def show():
#         print("ТЕСТ")

# python_checker = PythonChecker("Функция в Python")
# sql_checker = SQLChecker("SELECT запросы")
# react_checker = ReactChecker("React hooks")
# # java_checker = JavaChecker("React hooks")

# print(python_checker.check("def(a,b): return a + b"))
# print(sql_checker.check("SELECT * FROM users"))
# print(react_checker.check("const [count,setCount] = useState(0)"))
# java_checker.show()

# 2. Второй пример АБСТРАКЦИЯ

# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def work(self):
#         print(f"{self.name} работает")

# class Eat(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Sleep(ABC):
#     @abstractmethod
#     def sleep(self):
#         pass

# class Human(Person,Sleep,Eat):
#     def __init__(self,name,soul):
#         super().__init__(name)
#         self.soul = soul
    
#     def is_alive(self,soul):
#         print(f"{self.name} у него есть душа {self.soul}")

#     def eat(self):
#         print(f"{self.name} может кушать")

#     def sleep(self):
#         print(f"{self.name} может спать")
    


# class Robot(Person):
#     def __init__(self,name,ai):
#         super().__init__(name)
#         self.ai = ai

#     def is_ai(self,ai):
#         print(f"{self.name} робот с ai {self.ai}")


# human = Human("Alex", "Да")
# robot = Robot("Gemini", "Да")

# human.eat()
# human.sleep()
# human.is_alive("Да")
# human.work()

# robot.work()
# robot.is_ai("Да")



# Полиморфизм - это когда разные обьекты можно использовать одинаково

class AssigmentChecker(ABC):
    def __init__(self,title):
        self.title = title
    
    @abstractmethod
    def check(self,solution):
        pass
    
    def show_start_message(self):
        print(f"Это стартвое сообщение {self.title}")

class PythonChecker(AssigmentChecker):
    def check(self,solution):

        if "def" in solution and "return" in solution:
            return "Python-задание принято"
        return "Python-задание нужно доработать"

class SQLChecker(AssigmentChecker):
    def check(self,solution):
        upper_solution = solution.upper()

        if "SELECT" in upper_solution and "FROM" in upper_solution:
            return "SQL-задание принято"
        return "SQL-задание нужно доработать"

class ReactChecker(AssigmentChecker):
    def check(self,solution):
        if "useState" in solution or "useEffect" in solution:
            return "React-задание принято"
        return "React-задание нужно доработать"

class JavaChecker(AssigmentChecker):
    def show():
        print("ТЕСТ")

python_checker = PythonChecker("Функция в Python")
sql_checker = SQLChecker("SELECT запросы")
react_checker = ReactChecker("React hooks")
# java_checker = JavaChecker("React hooks")

print(python_checker.check("def(a,b): return a + b"))
print(sql_checker.check("SELECT * FROM users"))
print(react_checker.check("const [count,setCount] = useState(0)"))
# java_checker.show()

checkers = [
    PythonChecker("Функция в Python"),
    SQLChecker("SELECT запросы"),
    ReactChecker("React hooks")
]
solutions = [
    "def(a,b): return a + b",
    "SELECT * FROM users",
    "const [count,setCount] = useState(0)" 
]

for checker, solution in zip(checkers,solutions):
    checker.show_start_message()
    result = checker.check(solution)
    print(result)
    print("-" * 30)

