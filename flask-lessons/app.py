from flask import Flask

app = Flask(__name__)

# Маршрут
@app.route("/")
def home():
    return "Flask server is working"

python -m venv .venv
.venv/Scripts/activate
deactivate
pip install Flask
python -m pip list
python -m flask --app app run --debug