
from _11_Packages_Modules.abc.data1 import x, eid, name, sal, get_data
print("Variable : ", x)
print("Emp ID : ", eid)
print("Name   : ", name)
print("Sal    : ", sal)
print("Function call : ", get_data())


from _11_Packages_Modules.abc import data1
print("Variable : ", data1.x)
print("Emp ID : ", data1.eid)
print("Name   : ", data1.name)
print("Sal    : ", data1.sal)

print("Function call : ", data1.get_data())