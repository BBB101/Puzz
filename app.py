import hashlib
import re
import searches
from flask import (Flask, render_template, request, redirect, session)
from DB import DB as db

import sqlite3

app = Flask(__name__)
app.secret_key = "fe64b47d64e7b3f1a287382122a04eb15c778483cfa18705"


def hash_passwd(passwd):
    """return hashed 256 string"""
    m = hashlib.sha256()
    m.update((passwd+"dRgClDT").encode())
    return m.hexdigest()


@app.route('/')
def hello_world():
    """Returns Login Page"""
    return render_template('Login.html')


@app.route('/Search', methods=['POST', 'GET'])
def search():
    """Searches In The Net for prices"""
    if request.method == 'POST':
        if session.get("user") is None:
            return "<h1>You Are Not Logged in</h1><a href='/'>Login</a>"
        value = request.form.get('search')
        print(value)
        if len(value) == 0:
            return "<h1>Cannot Search Blank<h1><a href='/Home'>Back To Home</a>"
        #plans to create database with results not older than one day and check before searching through the internet
        dic = searches.AllSearch(value)
        dic2 = dict(sorted(dic.items(), key=lambda x: x[1]))  # sort by price
        s = ""
        klist = list()
        vlist = list()
        for k, v in dic2.items():
            klist.append(k)
            vlist.append(v)
#            s += "<tr><td>"+k+"</td><td>"+v+"</td></tr>" #an attempt to do the table dynamically
        session["sKeys"] = klist
        session["sValues"] = vlist
        return render_template('SearchResults.html')
    else:
        if session.get("username") is None:
            return "<h1>You Are Not Logged in</h1><a href='/'>Login</a>"


@app.route('/Register')
def Register():
    """Returns Register Page"""
    return render_template('Register.html')


@app.route('/RegAction', methods=['POST', 'GET'])
def RegisterAction():
    """Registers The User in The DB"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        email = request.form.get('mail')
        if len(username) == 0 or len(password) == 0:
            return "<h1>Cannot Enter Blank</h1><a href='/Register'>Back To Form</a>"
        if (bool(re.search('^[a-zA-Z0-9]*$', username)) == False or bool(re.search('^[a-zA-Z0-9]*$', password)) == False):# checking for bad letters
            return "<h1>Bad Letters</h1><a href='/Register'>Back To Form</a>"
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not bool(re.fullmatch(regex, email)):
            return "<h1>Bad Letters in Email</h1><a href='/Register'>Back To Form</a>"
        database = db()
        if database.query("SELECT * FROM USERS WHERE UNAME='"+username+"'"): #check for no duplicate users
            return "<h1>username is taken</h1><a href='/Register'>Back To Form</a>"
        if database.query("SELECT * FROM USERS WHERE UMAIL='"+email+"'"):
            return "<h1>user already exists<h1><a href='/Register'>Back To Form</a>"
        np = hash_passwd(password)
        success = database.Uquery("INSERT INTO USERS VALUES('"+username+"', '"+np+"', '"+email+"')")
        if success:
            return redirect('/')
        return "<h1>ERROR CREATING USER<h1><a href='/Register'>Back To Form</a>"


@app.route('/Home')
def Home():
    """Returns Homepage"""
    if session.get("user") is None:
        return "<h1>You Are Not Logged in</h1><a href='/'>Login</a>"
    return render_template('Home.html')


@app.route('/Logout')
def Logout():
    """Logs out the user"""
    if session.get("user") is None:
        return "<h1>You Are Not Logged in</h1><a href='/'>Login</a>"
    print("logout successful")
    session.pop('user', None)
    return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Signs The User In"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        print(username+","+password)
        if len(username) == 0 or len(password) == 0:
            return "<h1>Cannot Enter Blank</h1><a href='/'>Back To Login</a>"
        if (bool(re.search('^[a-zA-Z0-9]*$', username)) == False or bool(re.search('^[a-zA-Z0-9]*$', password)) == False):
            return "<h1>Bad Letters</h1><a href='/'>Back To Login Page</a>"
        print(password)
        np = hash_passwd(password)
        print(np)
        database = db()
        result = database.query("SELECT * FROM USERS WHERE UNAME='"+username+"' AND PASSWD='"+np+"'")
        if result:
            session['user'] = username
            return redirect('/Home')

        return "<h1>Wrong username or password</h1><a href='/'>Back To Login Page</a>"  # if the username or password does not matches

    return render_template("Login.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # if does not work  replace in running config --host=0.0.0.0
