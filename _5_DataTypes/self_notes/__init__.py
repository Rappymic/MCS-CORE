# list
list = [1,2,3,[1,2,3],(1,2,'a'),{1:23}]
print(list[3][1])
# tuple
tup = (1,2,3,[1,2,"a"],{1,2,3})
print(tup[4])
tup[3][2] = "b"
print(tup)
# list inside tuple is mutable

# set
set = {1,2,3,4,"a",(1,2,3)}
# set1 = {1,2,3,4,"a",(1,2,3),[1,2,3],{'abc':23}
# set doesn't support list and dictionary

# dictionary
dict1 = {'abc':[1,2,3], "[1,2,3]":{1,2,3},(1,2,3):{'abc':1},"{1,2,34}":12,"{1:2}":2}
print(dict1)
#