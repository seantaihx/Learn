#File Handling
'''
Allow you to work with file (open, read, write)
'''

#Open A File 
'''
format: open(path/filename, mode(optional))

mode:
"r": Read(Default). Open a file for reading, error if file doesnt exist 
"a": Append. Open a file for appending, create the file if doesnt exist
"w": Write. Open a file for writing, creates the file if doesnt exist
"x": Create. Creates a specified file, error if exists

Addition
't': Text(Default). Text mode
'b': Binary. Binary mode (for image and other)

ex: open('file_name.txt', 'rt')
ex: open('D:\\file\filename.txt')
'''

#Close A File
'''
format: filename.close()

if open the file using with statement, then no need to close it manually
format: with open(filename) as name
'''

#Read A File
'''
1. Read whole text or specific number of character
format:
with open ('filename.txt') as f:
  print(f.read(num_of_char))
  print(f.read())  #print whole text

2. Read one single line
format: 
f.readline
or
variable = f.readlines()
!!!.readlines() returns a list of lines

Or

use for loop to read a file line by line
format:
with open('filename.txt') as f:
  for i in f:
      print(i)
'''

#Write To Existing File
'''
format: 
with open ("file.txt", mode) as name:
  f.write(content)

mode:
"a": Append at the end of the file
"w": Clears the file when it opens it and write from the start

!!!In "w" mode, every previously existed thing will be clear as soon as the file is opened
'''

#Create A New File
'''
format: variable = open('filename.txt', 'x')
'''

#Delete A File
'''
Must import os module

format:
import os
os.remove('filename.txt')
'''

#Check If A File Exists
'''
Must import os module

format:
import os
if os.path.exists("filename.txt"):
  statement
else:
  statement
'''

#Delete A Folder
'''
Must import os module

format:
import os
os.rmdir("myfolder")

!!!Only can be used for empty folder
'''

