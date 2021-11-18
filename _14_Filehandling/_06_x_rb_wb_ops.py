# file = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt', 'rb')
# for i in file.readlines():
#     print(i)  # it will generate in byte format
# file.close()
#
# file3 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt', 'x')
# file3.write('hi')
# file3.close()  # it will show error as the file is already existing

file3 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file3.txt', 'x')
file3.write('hi')
file3.close()  # now it will create another file as it is not exist already

file3 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file3.txt', 'wb')
file3.write(
    b'good morning'
)
file3.close()  # In this way we can write the binary data into a file

'''
Pickling : converting the object data into bytes format (i.e using pickle.dump)
when we create a class and when we want to store that program into byte file than we create a object 
for that class and can process as below to convert to binary
pickle.dump(object,file)  file is the file where we want that binary data
it is also called as serializing

unpickling : converting the bytes data into object data (i.e using pickle.load)
pickle.load(object,file)
it is called de-serializing

'''

import pickle

file3 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file3.txt', 'wb')
file4 = {1: 'python', 2: 'java'}
pickle.dump(file4, file3)
file3.close()

file3 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file3.txt', 'rb')
a = pickle.load(file3)
print(a)


'''
seek(), tell()
seek method is used to set the file pointer at particular position so that read method will read from 
that point as below done
tell() will actually gives the position of the file pointer currently present

'''

file4 = open('file4.txt', 'w+')
file4.write('shiva prasad')
file4.seek(0)  # setting the position is zero
print(file4.read(2))  # read from zero + 1 position we get 'sh'
print(file4.tell())  # gives position number in file o/p : 2
file4.seek(6)  # setting position to 6
print(file4.read(6))  # reading from 6+1 pos we get o/p prasad
print(file4.tell())  # gives position number in file o/p : 12
file4.close()
