
from flask import Flask, render_template, sessions, url_for, session,request,redirect
import sqlite3
# from werkzeug import security

conn = sqlite3.connect('user.db', check_same_thread=False)
cur = conn.cursor()
app = Flask(__name__)
app.secret_key = "imvvvviabdjdnidnqinj"

# def upload_path(user1,file):
#     app.config['UPLOAD_FOLDER'] = f"/{user1}/"
#     file.save(secure_filename(file.filename))




def get_data():
    cur.execute(f"SELECT name, password FROM users")
    return cur.fetchall()

def dict_create(list1):
    dict1 = {}
    for i in list1:
        dict1[i[0]] = i[1]
    return(dict1)


dic = dict_create(get_data())
@app.route("/", methods = ['GET', 'POST'])
def home():
    if "user" in session:
        return redirect(url_for("user"))
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in dic:
            if dic[user] == password:
                session["user"] = user
                return redirect(url_for("user"))
            else:
                return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    return render_template('index.html')

@app.route("/user", methods = ['GET','POST'])
def user():
    if "user" in session:
        if request.method=="POST":
            # print(request.files)
            file = request.files['file']
            upload_path(user=session["user"])
            return "file uploded succesfully"
        return render_template("user.html")
    else:
        return redirect(url_for("home"))

if __name__== "__main__":
    app.run(debug=True, ssl_context='adhoc')
