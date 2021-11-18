
file1 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt','r')
print(file1.read(2))  # reads only two characters
print(file1.read(10)) # reads upto 10 chars only
print(file1.read()) # reads all data in the file
print(file1.readline()) # reads only 1 lines of file
print(file1.readline()) # in this case it reads both 1st and 2nd line

print(file1.readlines()) # returns list of lines of the file

for i in file1.readlines():
    print(i)       # printes the data of file line by line
file1.close()


file1 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt','r+')
for i in file1.readlines():
    print(i)
file1.write('''
hi shiva                           
good morning
i have been appended in this case
''')
file1.close()     # in this case the data inside write will be appended at the end every time when we execute
