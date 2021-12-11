import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()
# cur.execute("CREATE TABLE blog(title TEXT, body TEXT)")

conn.commit()
def create_blog(title, body):
    cur.execute(f"INSERT INTO blog VALUES('{title}', '{body}')")
    conn.commit()
    return "Done"

def update_blog(rowid, title, body):
    cur.execute(f"UPDATE blog SET title='{title}' WHERE rowid='{rowid}'")
    cur.execute(f"UPDATE blog SET body='{body}' WHERE rowid='{rowid}'")
    conn.commit()
    return "Done"

def delete(rowid):
    cur.execute(f"SELECT * FROM blog WHERE rowid='{rowid}'")
    if len(cur.fetchall()) == 0:
        return "Not Found"
    else:
        cur.execute(f"DELETE FROM blog WHERE rowid='{rowid}'")
        conn.commit()
        return "Done"

create_blog('venkat', 'somedata')