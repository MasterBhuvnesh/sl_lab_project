from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

TIMETABLE={
  "Monday": [
    { "time": "8:00-9:00", "subject": "Minor", "room": "DT-304" },
    { "time": "9:00-10:00", "subject": "HUT4003 - ME", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "CAT4002 - DAA", "room": "DT-206" },
    { "time": "11:00-12:00", "subject": "RECESS" },
    { "time": "12:00-1:00", "subject": "CAT4003 - TOC", "room": "DT-206" },
    { "time": "1:00-2:00", "subject": "CAT4001 - AI", "room": "DT-206" },
    { "time": "2:00-3:00", "subject": "MAT4001 - LA", "room": "DT-206" }
  ],
  "Tuesday": [
    { "time": "8:00-9:00", "subject": "OE", "room": "DT-304" },
    { "time": "9:00-10:00", "subject": "CAT4003 - TOC", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "CAT4002 - DAA", "room": "DT-206" },
    { "time": "11:00-12:00", "subject": "HUT4003 - ME", "room": "DT-206" }
  ],
  "Wednesday": [
    { "time": "8:00-9:00", "subject": "HUT4002 - EE", "room": "DT-206" },
    { "time": "9:00-10:00", "subject": "CAT4002 - DAA", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "RECESS" },
    { "time": "11:00-12:00", "subject": "CAT4001 - AI", "room": "DT-206" },
    { "time": "12:00-1:00", "subject": "MAT4001 - LA", "room": "DT-206" }
  ],
  "Thursday": [
    { "time": "8:00-9:00", "subject": "Minor", "room": "DT-304" },
    { "time": "9:00-10:00", "subject": "HUT4003 - ME", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "CAT4002 - DAA", "room": "DT-206" },
    { "time": "11:00-12:00", "subject": "RECESS" },
    { "time": "12:00-1:00", "subject": "CAT4003 - TOC", "room": "DT-206" },
    { "time": "1:00-2:00", "subject": "CAT4001 - AI", "room": "DT-206" }
  ],
  "Friday": [
    { "time": "8:00-9:00", "subject": "MAT4001 - LA", "room": "DT-206" },
    { "time": "9:00-10:00", "subject": "CAT4003 - TOC", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "RECESS" },
    { "time": "11:00-12:00", "subject": "HUT4002 - EE", "room": "DT-206" },
    { "time": "12:00-1:00", "subject": "CAT4002 - DAA", "room": "DT-206" }
  ],
  "Saturday": [
    { "time": "8:00-9:00", "subject": "HUT4003 - ME", "room": "DT-206" },
    { "time": "9:00-10:00", "subject": "CAT4002 - DAA", "room": "DT-206" },
    { "time": "10:00-11:00", "subject": "RECESS" },
    { "time": "11:00-12:00", "subject": "CAT4001 - AI", "room": "DT-206" },
    { "time": "12:00-1:00", "subject": "MAT4001 - LA", "room": "DT-206" }
  ]
}



@app.route('/')
def home():
    return render_template("timetable.html", timetable=TIMETABLE)

@app.route('/api/timetable')
def api_timetable():
    return jsonify(TIMETABLE)

if __name__ == '__main__':
    app.run(debug=True)
