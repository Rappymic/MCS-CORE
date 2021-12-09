import os
from flask import Flask, render_template,redirect,request, session, url_for
import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)
app.secret_key = "TESTKEY"
app.config["UPLOAD_FOLDER"] = "static/"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
def file_save(email, file):
    try:
        os.mkdir(f'/static/')
    except:
        pass
    file.save(file.filename)

def add_query(email, password,fname,lname,city,state,pin):
    return f'''INSERT INTO data VALUES('{email}','{password}','{fname}','{lname}','{city}','{state}','{pin}')'''

def get_query(email):
    return f"SELECT * FROM data WHERE email = '{email}'"

def all_query():
    return f"SELECT * FROM data"

def get_list(st):
    c.execute(st)
    return c.fetchall()

def dict_create(list1):
    dict1 = {}
    for i in list1:
        dict1[i[0]] = i[1]
    return(dict1)

def final():
    return dict_create(get_list(all_query()))

def full_details(list1):
    temp_dict={}
    for item in list1:
        temp_dict={'email':item[0],'First Name':item[2],'Last Name':item[3],'Location':item[4],'State':item[5],'Pin Code':item[6]}
    return temp_dict

def full_details1(list1):
    temp_dict={}
    for item in list1:
        temp_dict={'email':item[0],'fname':item[2],'lname':item[3],'location':item[4],'State':item[5],'Pin':item[6]}
    return temp_dict

@app.route('/', methods=['GET','POST'])
def home():
    if 'email' in session:
        return redirect(url_for('show_detail'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in final():
            if password == final()[email]:
                session["email"] = email
                return redirect(url_for("show_detail"))
            else:
                return "Invalid login"
    return render_template("index.html")

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        location = request.form['location']
        state = request.form['state']
        pin = request.form['pin']
        c.execute(add_query(email=email,password=password,fname=fname,lname=lname,city=location,state=state,pin=pin))
        conn.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/show_detail', methods=['GET','POST'])
def show_detail():
    if "email" in session:
        if request.method=="POST":
            f = request.files['file']
            file_save(email=session['email'], file=f)
            return redirect(url_for('show_detail'))
        return render_template('show.html',alldata=full_details(get_list(get_query(session['email']))))
    else:
        return "USER NOT LOGGED IN"

@app.route('/logout')
def logout():
    session.pop('email')
    return redirect(url_for("home"))

@app.route('/update')
def update():
    if 'email' in session:
        return render_template('update.html', alldata=full_details1(get_list(get_query(session['email']))))
    else:
        return 'Not Logged in'

if __name__ == "__main__":
    app.run(debug=True)