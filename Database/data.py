import sqlite3


def insert_details(cursor, table_name, fname, lname, identity):
    cursor.execute(f"INSERT INTO {table_name} VALUES('{fname}','{lname}','{identity}')")

list1 = [{'fname':'Venkat','lname':'Reddy','id':43},{'fname':'Satish','lname':'Katta','id':89}]
with sqlite3.connect("newdb.db") as conn:
    a_cursor = conn.cursor()
    # a_cursor.execute("CREATE TABLE details(fname TEXT,lname TEXT,id INTEGER) ")
    # for index, values in enumerate(list1):
    #     insert_details(a_cursor, table_name='details', fname=values['fname'], lname=values['lname'], identity=values['id'])
    a_cursor.execute("ALTER TABLE details DROP salary")
    conn.commit()
