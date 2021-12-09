# import sqlite3


# conn = sqlite3.connect("data.db")

# c= conn.cursor()

# # c.execute("CREATE TABLE data(email TEXT PRIMARY KEY, password TEXT, fname TEXT, lname TEXT, city TEXT, state TEXT, pin INT)")
# conn.commit()
# def add_query(email, password,fname,lname,city,state,pin):
#     return f'''INSERT INTO data VALUES('{email}','{password}','{fname}','{lname}','{city}','{state}','{pin}')'''

# def get_query(email):
#     return f"SELECT * FROM data WHERE email = '{email}'"
# c.execute(add_query('kartik@gmail.com','password','kartik','paliwal','banglore','karnatak',282005))
# conn.commit()

# c.execute(get_query('kartik@gmail.com'))
# def add_query(email, password,fname,lname,city,state,pin):
#     return f'''INSERT INTO data VALUES('{email}','{password}','{fname}','{lname}','{city}','{state}','{pin}')'''

# def get_query(email):
#     return f"SELECT * FROM data WHERE email = '{email}'"

# def all_query():
#     return f"SELECT * FROM data"

# def get_list(st):
#     c.execute(st)
#     return c.fetchall()

# def dict_create(list1):
#     dict1 = {}
#     for i in list1:
#         dict1[i[0]] = i[1]
#     return(dict1)

# final_dict = dict_create(get_list(all_query()))
# print(final_dict)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

print(BASE_DIR)