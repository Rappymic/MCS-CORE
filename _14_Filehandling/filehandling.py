"""
Modes of opening file in Python:
There are many modes of opening a file in Python, unlike other languages
Python has provided its users a variety of options. We will discuss seven of
them in this tutorial.

r : r mode opens a file for read-only. We do not have permission to update or
    change any data in this mode.
w : w mode does not concern itself with what is present in the file.
    It just opens a file for writing and if there is already some data present
    in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing
    file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file.
    It does exactly the same. It just adds the data we like in write(w) mode
    but instead of overwriting it just adds it to the end of the file.
    It also does not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text
    files can be opened by it. It deals with the file data as a string.
b : b stands for binary and this mode can only open the binary files, that are
    read in bytes. The binary files include images, documents, or all other
    files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is
    mostly used in cases where we want to update our file.

open file
_________________
open("filename" ,"mode")
To open a file, we must specify two things,

Name of the file and its extension
Access mode where we can specify in which mode file has to be opened, it could
either be read (r), write (w) or append(a), etc. For more information regarding
access modes, refer to the previous tutorial.
For Example,

open("myfile.txt")
The file “myfile.txt” will open in "rt" mode as it is the default mode. But
the best practice is to follow the syntax to avoid errors.

The open function returns a file object. We store this file object into a
variable which is generally called as a file pointer/file handler. Here is a
code snippet to open the file using file handing in Python,

  f=open("myfile.txt," "w")
You can use this file pointer to further add modifications in the file. An
error could also be raised if the operation fails while opening the file.
It could be due to various reasons like trying to access a file that is already
closed or trying to read a file open in write mode.



Read a file
______________
To read a file in Python, there are various methods available,
We can read a whole file line by line using a for loop in combination with an
iterator. This will be a fast and efficient way of reading data.
When opening a file for reading, Python needs to know exactly how the file
should be opened. Two access modes are available reading (r), and reading in
binary mode (rb). They have to be specified during opening a file with the
built-in open() method.
f = open("myfile.txt", "r")
The read() method reads the whole file by default. We can also use the
read(size) method where you can specify how many characters we want to return
i.e.
f.read(2); #Here, you will get the first two characters of the file.
You can use the readline() method to read individual lines of a file. By
calling readline() a second time, you will get the next line.
readlines() method reads until the end the file ends and returns a list of
lines of the entire file. It does not read more than one line.
f=open("myfile.txt","r");
f.readlines() #Returns a list object
Note: The default mode to read data is text mode. If you want to read data in
binary format, use ''rb".

Close a File
__________________

it is always the best practice to close a file after you are done performing
operations on it. However, Python runs a garbage collector to clean up the
unused objects, but as good programmers, we must not rely on it to close the
file. Python has a build-in close() function to close a file i.e;

f.close()

seek()
When we open a file, the system points to the beginning of the file. Any read
or write will happen from the start. To change the file object’s position, use
seek(offset, whence) function. The position will compute by adding offset to a
reference point, and the whence argument selects the reference point. It is
useful when operating over an open file. If we want to read the file but skip
the first 5 bytes, open the file, use function seek(5) to move to where you
want to start reading, and then continue reading the file.
"""