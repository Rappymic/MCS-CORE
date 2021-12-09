import sqlite3

conn = sqlite3.connect("user.db")

cur = conn.cursor()

cur.execute(f"CREATE TABLE kartik(file BLOB)")
# cur.execute("INSERT INTO users VALUES('kartik1','password')")
def get_data():
    cur.execute(f"SELECT name, password FROM users")
    return cur.fetchall()

print(get_data())

def dict_create(list1):
    dict1 = {}
    for i in list1:
        dict1[i[0]] = i[1]
    return(dict1)

print(dict_create(get_data()))

conn.commit()