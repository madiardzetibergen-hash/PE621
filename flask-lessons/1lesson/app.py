from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "title": "Python Basics",
        "duration": 3
    },
    {
        "id": 2,
        "title": "Frontend basics",
        "duration": 4
    },
    {
        "id": 3,
        "title": "Git/Github",
        "duration": 0.5
    }
]

@app.get("/courses")
def get_courses():
    return jsonify(courses)

@app.get("/courses/<int:course_id>")
def get_course_by_id(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course)
    return jsonify({
        "error": "Course not found"
    }),404




# Маршрут
@app.route("/")
def home():
    return "Главная страница"

@app.route("/about")
def about():
    return "Это первый раз в Flask"


@app.route("/status")
def server():
    return "Сервер работает"

# @app.route("/profile/alex")
# def alex_profile():
#     return "Alex"

@app.route("/profile/<name>")
def profile(name):
    return f"Profile: {name}"

@app.route("/course/<title>/<int:course_id>")
def course(course_id, title):
    return f"{course_id}:{title}"

@app.route("/calculate/<operation>/<int:a>/<int:b>")
def calculate(operation,a,b):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a -b 
    elif operation == "multiply":
        result = a * b 
    elif operation == "divide":
        if b == 0:
            return "Division by zero is not allowed"
        result = a / b
    else:
        return "Unknown operation"
    return str(result)



@app.route("/info")
def info():
    project = {
        "name": "Fullcycle",
        "language": "Python",
        "project": "e-shop",
        "status": "to-do"
    }
    return jsonify(project)