from flask import Flask, jsonify, render_template, request, session, redirect, url_for
import os
import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

app = Flask(__name__)
app.secret_key = "FU"


def get_data():
    cur.execute("SELECT username, password FROM users")
    return cur.fetchall()


def dict_return(list1):
    dict1 = {}
    for i in list1:
        dict1[i[0]] = i[1]
    return dict1


final_dict = dict_return(get_data())


def logined(fuct):
    def wrapper():
        if session:
            output = fuct()
            return output
        else:
            return redirect(url_for("home"))

    return wrapper


@app.route("/", methods=["GET", "POST"])
def home():
    # print(session["user"])
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        if user in final_dict:
            if password == final_dict[user]:
                session['user'] = user
                return redirect(url_for("user"))
            else:
                return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    return render_template('index.html')


@app.route("/user")
def user():
    if "user" in session:
        return "you have been logined"
    else:
        return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug=True)
