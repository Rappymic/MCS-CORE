import os

# checking whether the file is already present or not

if os.path.exists('file4.txt'):  # here as file is present than the file will get overridden
    f = open('file4.txt', 'w')
    f.write('hi shiva, yes this file exist already')
    f.close()
else:
    print('file does not exist')

print(os.getcwd())  # o/p will be path of the present working directory

# os.remove('file3.txt') # it removes the file

size = os.path.getsize('file4.txt')
print(size)  # this method gives the size based on number of upto characters position present

print(os.listdir(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes'))
