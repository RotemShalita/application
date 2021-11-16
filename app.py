from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

def get_jsons():
    students_dir = "..\\wis-advanced-python-2021-2022\\students"
    return [(json.load(open(os.path.join(students_dir, i))), os.path.join(students_dir, i)) for i in os.listdir(students_dir)]

@app.route("/")
def main():
    names = []
    for student, path in get_jsons():
        names.append((student["name"], path))

    print(names)
    return render_template('app.html', names=names)

@app.route("/search", methods=['POST'])
def search():
    if not 'text' in request.form:
        return "Bad search value"
    searched_str = request.form['text'].lower()

    searched_list = []
    for student, _ in get_jsons():
        if searched_str in student["name"].lower():
            searched_list.append([student["name"]])

    return render_template('app.html', names=searched_list)

@app.route("/user/<uid>")
def api_info(uid):
    for student, path in get_jsons():
        if student["name"] == uid:
            return student

@app.route("/user/")
def user():
    return 'Please search for a student' 