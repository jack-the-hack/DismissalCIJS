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

from collections import defaultdict
from flask import Flask, render_template, request, redirect, session, make_response
import sqlite3
import os
import atexit
import sys
import signal

nxt1 = False
nxt2 = False
nxt3 = False
Name = "No one yet!"
oldName1, oldName2, oldName3 = "", "", ""
LST = defaultdict(list)
App = Flask(__name__)
App.secret_key = os.environ['KEY']
DataBase = sqlite3.connect(
    'Database/Students.db',
    check_same_thread=False,
    isolation_level=None)
cur = DataBase.cursor()
print(os.system("ls"))
user = {"username": "cjs333", "password": "cijs321studentgobye"}
listfile=open("Teachers.jslos",'r+')
Teachers = listfile.read().split('%5$^^')
insert = ""
print(Teachers)
for Teacher in Teachers:
    insert += f"<option value=\"{Teacher}\">{Teacher}</option>"
dropdown = f"<form method=\"POST\"><select id=\"Teacher\" name=\"Teacher\" required> {insert}</select><input type=\"submit\"/></form>"

def checkmaxidplus1():
    cur.execute("SELECT MAX(ID) FROM Students")
    ttt = cur.fetchall()[0][0]
    return ttt + 1


def Addstudent(ID: int, Name: str, Teacher: str, Grade: int, IsMe: bool):
    open("tt", 'w').write("2")
    cur.execute("INSERT INTO Students VALUES (?,?,?,?,?)",
                (ID, Name, Teacher, Grade, IsMe))
    DataBase.commit()


def dismiss(ID):
    cur.execute("SELECT * FROM Students GROUP BY ID HAVING ID=?", (ID,))
    Fulldataa = cur.fetchall()
    if len(Fulldataa) == 1:
        Fulldata = Fulldataa[0]
        try:
            LST[Fulldata[2]].append(Fulldata[1])
        except BaseException:
            LST[Fulldata[2]] = [Fulldata[1]]
        return 1
    else:
        return False


@App.route("/")
def rdrct():
    return "test"


@App.route("/Teacher/", methods=["GET", "POST"])
def Teacher():
    print(LST)
    Name = "No one yet!"
    oldName1, oldName2, oldName3 = "", "", ""
    nxt1 = False
    nxt2 = False
    nxt3 = False
    if request.method == 'POST':
        Tchr = request.form['Teacher']
        resp = make_response(render_template('Teacher.html'))
        resp.set_cookie('who', Tchr,expires=189356040000)
        return resp
    else:
        cookie = request.cookies.get("who")
        if cookie not in Teachers:
          resp = make_response(render_template('Teacher.html'))
          resp.set_cookie('who', "",expires=0)
        if cookie != "" and cookie in LST:
            Name = LST[cookie][-1]
            nxt1 = True
        if nxt1 and len(LST[cookie]) >= 2:
            oldName1 = LST[cookie][-2]
            nxt2 = True
        if nxt2 and len(LST[cookie]) >= 3:
            oldName2 = LST[cookie][-3]
            nxt3 = True
        if nxt3 and len(LST[cookie]) >= 4:
            oldName3 = LST[cookie][-4]
        return render_template(
            "Teacher.html",
            Name=Name,
            oldName1=oldName1,
            oldName3=oldName3,
            dropdown=dropdown)


@App.route("/Scanner/", methods=["POST", "GET"])
def Scanner():
    if request.method == "POST":
        ID = request.form['ID']
        worked = dismiss(ID)
        return render_template(
            "Scanner.html", Notif=[
                "" if worked else "Did not recognise."][0])
    else:
        return render_template("Scanner.html")

# Step – 4 (creating route for login)


@App.route('/admin/', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/lmrwqqrthhs/')
        else:  # if the username or password does not matches
            return "<h1>Wrong username or password</h1>"
    else:
        return render_template("login.html")


@App.route('/lmrwqqrthhs/')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return render_template("dashboard.html", dropdown=dropdown)
    else:
        return '<h1>You are not logged in.</h1>'


@App.route("/newstudent/", methods=["POST"])
def newstudent():
    Name = request.form.get("name")
    Teacher = request.form.get("Teacher")
    Grade = request.form.get("grade")
    Id = checkmaxidplus1()
    open("tt", 'w').write("1")
    print(Id)
    Addstudent(Id,Name,Teacher,Grade,False)
    return redirect("/lmrwqqrthhs/")
@App.route("/quit/")
def quit():
  DataBase.close()
  kkk=""
  for i in Teachers:
    kkk+=i+"%5$^^"
  kkk=kkk[:-5]
  listfile.close()
  listfile2=open("Teachers.jslos",'w')
  listfile2.write(kkk)
  open('tt','w').write(str(Teachers))
  open("tt",'w').write(str(Teachers))
  os.kill(os.getpid(),signal.SIGKILL)
  return "failed"
@App.route("/newteacher/", methods=["POST"])
def newteacher():
    Teachers.append(request.form.get('Teacher'))
    return redirect("/lmrwqqrthhs/")
@App.route("/swtchteacher/", methods=["POST"])
def swchteacher():
    global Teachers
    Teachers.remove(request.form.get('Teacher'))
    Teachers.append(request.form.get('NewTeacher'))
    cur.execute("UPDATE Students SET Teacher=? WHERE Teacher=?",(request.form.get('NewTeacher'),request.form.get('Teacher')))
    return redirect("/lmrwqqrthhs/")
App.run('0.0.0.0')
