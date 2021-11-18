file1 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt', 'w')
file1.write('hi shiva \n')
file1.write('how are you \n')
file1.writelines('welcome to 1t file, you can see how we can write the file')
file1.close()



file2 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file2.txt','w')
file2.write(''' r ', for reading.
' w ', for writing.
' a ', for appending.
' r+ ', for both reading and writing
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()''')
file2.close()


# when we do write operation on same file then the previous data is overridden by new data

file2 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file2.txt','w')
file2.write('''
rstrip(): This function strips each line of a file off spaces from the right-hand side.
lstrip(): This function strips each line of a file off spaces from the left-hand side.
''')
file2.close()

# we can perform write and read operations on file by using w+ mode

file2 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file2.txt','w+')
file2.write('''
We can also split lines using file handling in Python. This splits the variable when space is encountered.
You can also split using any characters as we wish. Here is the code:

# Python code to illustrate split() function
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
''')
file2.seek(0)
data = file2.readlines()
for i in data:
    print(i)
file2.close()
