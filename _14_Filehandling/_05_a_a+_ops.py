
file1 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file1.txt','a')
file1.write('''
i am the new data adding at the end of existing data in a file
i hope it is clear
thank you
''')
file1.close()


'''
in this case the existing data inside the file will not be overridden instead of that it will be adding
at the end of the existing data in the file.
and this adding process will continue once again when ever we execute the same code
'''

file2 = open(r'E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\file2.txt','a+')
file2.write('''
hi shiva 
i am the new data added in this file2
by using a+ mode you can add data and read the data in the file
thank you
''')
file2.seek(0)    # seek method will offset the mode for append to read mode here
print(file2.read())
file2.close()


