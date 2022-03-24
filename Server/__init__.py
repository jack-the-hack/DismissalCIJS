''' This program is meant for use by schools for dismissal of students via bar code scanner.

Copyright (C) 2022  Donnie Jack Baldyga

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
Name = "No one yet!"
IDLST = []
App = Flask(__name__)
App.secret_key = os.environ['KEY']
DataBase = sqlite3.connect('../Database/Students.db')
cur = DataBase.cursor()
print(os.system("ls"))
user = {"username": "cjs333", "password": "cijs321studentgobye"}


def Addstudent(ID: int, Name: str, Teacher: str, Grade: int, IsMe: bool):
    cur.execute(
        f"INSERT INTO Students VALUES ({ID},{Name},{Teacher},{Grade},{IsMe})")


def dismiss():
    ID=IDLST[-1]
    cur.execute(f"SELECT * FROM Students GROUP BY ID HAVING ID={ID}")
    Fulldata=cur.fetchall()
    


@App.route("/Teacher/")
def Teacher():
    return render_template("Teacher.html", Name=Name)


@App.route("/Scanner/", methods=["POST", "GET"])
def Scanner():
    if request.method == "POST":
        ID = request.form['ID']
        IDLST.append(ID)
        print(IDLST)
        return render_template("Scanner.html")
    else:
        return render_template("Scanner.html")

# Step – 4 (creating route for login)


@App.route('/admin', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:

            session['user'] = username
            return redirect('/lmrwqqrthhs')

        # if the username or password does not matches
        return "<h1>Wrong username or password</h1>"

    return render_template("login.html")


@App.route('/lmrwqqrthhs')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return render_template("dashboard.html")
    # here we are checking whether the user is logged in or not
    else:
        return '<h1>You are not logged in.</h1>'


App.run(host='0.0.0.0')
