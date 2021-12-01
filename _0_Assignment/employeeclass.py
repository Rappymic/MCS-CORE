dictionary1 = {'A': [{'identity': 1, 'name': 'Kartik Paliwal',
                      'salary': {'Basic': 100000, 'HRA': 1000, 'SA': 1000}},
                     {'identity': 2, 'name': 'Venkat',
                      'salary': {'Basic': 20000, 'HRA': 1000, 'SA': 1000}}
                     ],
               'B': [{'fname': 'Kartik', 'lname': 'Paliwal', 'location': 'Bangalore',
                      'salary': {'Basic': 10000, 'HRA': 1000, 'SA': 1000}, 'identity': 1
                      },
                    {'fname': 'Bhavesh', 'lname': 'Shetty', 'location': 'Maysore',
                      'salary': {'Basic': 1000, 'HRA': 1000, 'SA': 1000}, 'identity':21
                      },
                     ]
               }


def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False


def sum_list(dict1):
    sum = 0
    for item in dict(dict1).values():
        sum = sum + item
    return sum


class EmployeeA:
    def __init__(self, identity, salary, name=None):
        self.name = name
        self.identity = identity
        self.salary = salary

    def print_even_details(self):
        if even_check(self.identity) == True:
            print(f"ID is {self.identity} and name is {self.name}")

    def emp_data(self):
        return f"The employee name is {self.name}, id is {self.identity} and salary is {sum_list(self.salary)}"

    def emp_salary(self):
        return f"The salary of {self.name} is {sum_list(self.salary)}"


class EmployeeB(EmployeeA):
    def __init__(self, fname, lname, salary, identity, location):
        super().__init__(salary=salary, identity=identity, name=fname +" "+ lname)
        self.fname = fname
        self.lname = lname
        self.identity = identity
        self.location = location

    def print_salary_more_than_10000(self):
        if sum_list(self.salary) > 10000:
            print(f"The employee {self.name} has salary of {sum_list(self.salary)} is greater than 10000")

    def sal_emp(self):
        return f"Salary: {sum_list(self.salary)} --- Name: {self.name}"

    def loca(self):
        return f"The ID is {self.identity} and Location is {self.location}"


emp_A = dictionary1['A']
name_A = []
for item in emp_A:
    name_A.append(item['name'])

emp_B = dictionary1['B']
name_B = []
for item in emp_B:
    name_B.append(item['fname'])

instance_listA = []
i = 0
for name in name_A:
    name = EmployeeA(identity=emp_A[i]['identity'], salary=emp_A[i]['salary'], name=emp_A[i]['name'])
    i += 1
    instance_listA.append(name)
instance_listB = []
i = 0

for name in name_B:
    name = EmployeeB(fname=emp_B[i]['fname'],lname=emp_B[i]['lname'], location=emp_B[i]['location'], salary=emp_B[i]['salary'], identity=emp_B[i]['identity'])
    instance_listB.append(name)
    i+=1

print(f"Class A".center(80, "-"))
for obj in instance_listA:
    obj.print_even_details()
    print(obj.emp_data())
    print(obj.emp_salary())
print(f"Class B".center(80, "-"))
for obj in instance_listB:
    obj.print_salary_more_than_10000()
    print(obj.emp_data())
    print(obj.emp_salary())
    print(obj.sal_emp())
    print(obj.loca())

