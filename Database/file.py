import sqlite3

conn = sqlite3.connect("customer.db")
# create a cursor
c = conn.cursor()
# create a table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#         )""")
# many_customers = [('West','Brown','west@brown.com'),
#                   ('steph', 'Kuewa', 'steph@hj.com'),
#                   ('Dan', 'Pas', 'dan@pas.com')]
# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)
"""
- NULL
- INTEGER
- REAL
- TEXT
- BLOB
"""
c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
# c.fetchone()
# c.fetchmany()
for items in c.fetchall():
    print(items)

# commit
conn.commit()
# close our connection
conn.close()