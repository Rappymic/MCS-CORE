
print("Start of program")   # logging in projects
num = 1
while num <= 10:   # Each iteration
    print(num)
    num += 1
print("End of program")


class Employee:
    pass

def get_data():
    pass


list1 = [1, 12, 10, 22, 44, 3, 34, 10, 5, 66, 6, 10, 7, 88, 18, 9, 100]

print("Before list  :", list1)
for val in list1:
    if val % 2 == 0:
        list1.remove(val)
print("After list   :", list1)
print("----------------------------------")


print("Before list  :", list1)
li2 = []
for val in list1:
    if val % 2 == 0:
        li2.append(val)
print("To be removed :",li2)
print("After list   :", list1)




'''
Production issue occurance : Live environment / Production environment
Issue will be reported by customer 
Ticket to developer 
 - I. Replicate(reproduce) the issue 
        - Issues Exists
            - 1.2 Root cause analysis (Find what is the reason for issue) # DEBUGGING
            - 1.3 Fix the issue
            - 1.4 Testing  (Local, DEV, Test, UAT ) instances
            - 1.5 Deploy to production instance 
        - Issue doesnt exist
            - Return mail to customer
'''