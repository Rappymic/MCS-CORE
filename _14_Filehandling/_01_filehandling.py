'''
File handling:
Python too supports file handling and allows users to handle files i.e., to read and write files,
along with many other file handling options, to operate on files.
In python there are two types of files:
text files
binary files
In text files the data is store in the form of characters or strings but in
binary files the data is stored in the form of bytes. when we want to retrieve data from binary file,
we can retrieve the data as bytes. binary files can be used to store text, images, audio, video.
We use open () function in Python to open a file in read or write mode
syntax:
        open(filename, mode)

different types of modes in opening file:
r : read data from the file
w : write data into file. if we do write operation on existing file all the previous data will be overrides by new data
a : appending or adding new data at the end of existing file
w+ : to write and read data into a file
r+ : to read and write data into file
a+ : to append and read data of a file
x : to open file in creation mode.the file creation fails if the file already exist.

after opening the file and doing some crud operations on file at the end we have to close the file using close method

f = open('filename','r')
f.read()
--------
--------
f.close()

'''
