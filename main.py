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
import time
import os
Name = "No one yet!"
IDLST = []
App = Flask(__name__)
App.secret_key=os.environ['KEY']
DataBase = sqlite3.connect('Students.db')
cur = DataBase.cursor()
print(os.system("ls"))
user = {"username": "cjs333", "password": "cijs321studentgobye"}

def dismiss():
    pass


@App.route("/Teacher/")
def Teacher():
    r = 0
    return render_template("Teacher.html", Name=Name)


@App.route("/Scanner/", methods=["POST", "GET"])
def Scanner():
    if request.method == "POST":
        ID = request.form['ID']
        IDLST.append((time.time(), ID))
        print(IDLST)
        return render_template("Scanner.html")
    else:
        return render_template("Scanner.html")
      
#Step – 4 (creating route for login)
@App.route('/admin', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('/lmrwqqrthhs')

        return "<h1>Wrong username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")
@App.route('/lmrwqqrthhs')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return render_template("dashboard.html")
    #here we are checking whether the user is logged in or not

    return '<h1>You are not logged in.</h1>'  #if the user is not in the session

App.run(host='0.0.0.0')
