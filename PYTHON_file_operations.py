#!/usr/bin/env python3
import os

# printing the header #
print("Welcome to file management script")
print('*' * 30)
print('')

# input the name and mode of file - strings allowed #
filename = input("Enter the absolute name of the file: ")
filemode = input("Enter the mode in which you want to open above file: ")

custom_file = open(filename, filemode)
custom_file.close()

# insert content to a file #
print('')
print("Inserting some content to file")
custom_file = open(filename, 'w')
custom_file.writelines(['Hello Friends!!!\n', 'Welcome to Python Learning Session\n', 'We discussed below till now:\n', 'Introduction, Installation, Python Objects'])
custom_file.close()

# Reading content of file #
print('')
print("Reading the file content")
print('')
print('*' * 30)
count = 0
custom_file = open(filename, 'r')
for line in custom_file:
    count += 1
    print("lineNo: ", count, " - ", line)

custom_file.close()

# Appending extra lines to file at the end #
print('')
print('*' * 30)
print('')
print("Appending some extra lines")
custom_file = open(filename, 'a')
extrastring = input("Enter some extra content: ")
custom_file.write("\n")
custom_file.write(extrastring)
custom_file.close()

# Reading back the updated file #
print('')
print("Reading the updated file content")
count = 0
custom_file = open(filename, 'r')
for line in custom_file:
    count += 1
    print("lineNo: ", count, " - ", line)

custom_file.close()

# Adding line at specific position #
print('')
newline = int(input("Add the line number where you want to add: "))
newcontent = input("Add the content you want top enter: ")
pos = newline - 1

with open(filename, 'r+') as f:
    file_dump = f.readlines()

file_dump.insert(pos, newcontent+'\n')

with open(filename, 'r+') as f:
    f.writelines(file_dump)

print('')
print('Displaying the updated content')
print('*' * 30)
print('')
count = 0
with open(filename, 'r+') as f:
    for line in f:
        count += 1
        print("lineNo: ", count, " - ", line)



# Removing the file #
print('')
endfile = input("Please confirm if you want to delete this file(y/n): ")
if (endfile == 'y'):
    os.remove(filename)
    print("Deleting: ", filename)
else:
    print("File", filename, "is not deleted")