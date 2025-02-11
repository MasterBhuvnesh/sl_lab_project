from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_timetable():
    with open("timetable.json", "r") as file:
        return json.load(file)

TIMETABLE = load_timetable()

@app.route('/')
def home():
    return render_template("timetable.html", timetable=TIMETABLE)

@app.route('/api/timetable')
def api_timetable():
    return jsonify(TIMETABLE)

if __name__ == '__main__':
    app.run(debug=True)
