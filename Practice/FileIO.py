# # read entire file 

# f = open("sample.txt","r")
# data = f.read()
# print(data)
# print(type(data))


# # read one line at a time 

# line1= f.readline()
# line2=f.readline()
# print(line1)
# print(line2)

# # read all lines into a list

# lines=f.readlines()
# print(lines)

# # writing lines

# file = open('sample.txt',"w")
# file.write("hello,world!\n")
# file.write("This is new line")
# file.close()

# # write multiple lines 

# file = open("sample.txt", "w")
# lines = ["First line\n", "Second line\n", "Third line\n"]
# file.writelines(lines)  # Write multiple lines at once
# file.close()

# # appending datato a file 

# file = open("sample.txt","a")
# file.write("this is additional line.\n")
# file.close()

# # closing file

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)

# # working with os and pathlib

# import os
# print(os.getcwd())

# # pathlib - to work with paths

from pathlib import Path
file_path = Path(r'C:\Users\Viraj Gavas\OneDrive\Desktop\projects\python\learn_python\Learn Python Basic to advance\Practice\pop.txt')
with file_path.open("r") as file:
    print(file.read())


# handline file exceptions

try:
    file = open("missing.txt","r")
    content= file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: file not found.")