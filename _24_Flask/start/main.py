import sqlite3

conn = sqlite3.connect("data.db")
cur= conn.cursor()
# comm.execute("CREATE TABLE users(username TEXT PRIMARY KEY, password TEXT)")
# comm.execute("INSERT INTO users VALUES('paliwal','password')")
conn.commit()
def get_data():
    cur.execute("SELECT username, password FROM users")
    return cur.fetchall()
print(get_data())