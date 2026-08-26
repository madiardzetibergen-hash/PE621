from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Замените postgres, password и my_database на ваши данные
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:123@localhost:5432/students'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
  __tablename__ = 'students'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gpa = db.Column(db.Numeric(3, 2), nullable=False)

  def to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gpa': float(self.gpa),
    }


# 1. Получить всех студентов (с сортировкой)
@app.route('/students', methods=['GET'])
def get_students():
  sort_by = request.args.get('sort_by', 'id')
  order = request.args.get('order', 'asc')

  column = getattr(Student, sort_by, Student.id)

  query = Student.query
  if order.lower() == 'desc':
    query = query.order_by(column.desc())
  else:
    query = query.order_by(column.asc())

  students = query.all()
  return jsonify([s.to_dict() for s in students])


# 2. Получить конкретного студента по ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
  student = Student.query.get_or_404(student_id)
  return jsonify(student.to_dict())


# 3. Добавить нового студента
@app.route('/students', methods=['POST'])
def create_student():
  data = request.get_json()

  if not data or not all(k in data for k in ('name', 'age', 'gpa')):
    return (
        jsonify({'error': 'Необходимы поля: name, age, gpa'}),
        400,
    )

  new_student = Student(name=data['name'], age=data['age'], gpa=data['gpa'])
  db.session.add(new_student)
  db.session.commit()

  return jsonify(new_student.to_dict()), 201


# 4. Обновить данные студента
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
  student = Student.query.get_or_404(student_id)
  data = request.get_json()

  if 'name' in data:
    student.name = data['name']
  if 'age' in data:
    student.age = data['age']
  if 'gpa' in data:
    student.gpa = data['gpa']

  db.session.commit()
  return jsonify(student.to_dict())


# 5. Удалить студента
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
  student = Student.query.get_or_404(student_id)
  db.session.delete(student)
  db.session.commit()

  return jsonify({'message': f'Студент с ID {student_id} удален'})


if __name__ == '__main__':
  app.run(debug=True)