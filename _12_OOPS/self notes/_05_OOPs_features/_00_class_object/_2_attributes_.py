class Employee:
    '''This class give details about employee'''
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_data(self):
        print("Employee data : ", self.eid, self.name, self.sal)

# Built in class attributes '''
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

# CRUD - Create Retrieve Update Delete

madhu = Employee(100, "Madhu N", 10000)  # CREATE

'''
setattr : To set IV value inside object  # UPDATE
getattr : To retrieve IV value           # RETRIEVE 
hasattr : To check IV has specific value # RETRIEVE
delattr : To delete IV                   # DELETE   
'''
print("------------getter------------------------")
# getter - RETRIEVE
print("Madhu name :", getattr(madhu, "name"))
print("Madhu eid  :", getattr(madhu, "eid"))
# print("Madhu addr  :", getattr(madhu, "addr"))

print("------------setter------------------------")
# setter - UPDATE
print("Setting name :", setattr(madhu, "name", "MAD"))
print("Setting eid  :", setattr(madhu, "eid", 200))
print("Setting addr :", setattr(madhu, "address", 'Bangalore'))

print("Get name:", getattr(madhu, "name"))
print("Get eid :", getattr(madhu, "eid"))
print("Get addr:", getattr(madhu, "address"))

print("------------hasattr------------------------")
print("Has attr sal :", hasattr(madhu, "sal"))
print("Has attr addr:", hasattr(madhu, "address"))
print("Has attr loc :", hasattr(madhu, "location"))

print("------------delattr------------------------")
print("Delete attr :", delattr(madhu, "sal"))
print(getattr(madhu, "sal"))
