#!/usr/bin/env python3
import os

# printing the header #
print("Welcome to file management script")
print('*' * 30)
print('')

# input the name and mode of file - strings allowed #
filename = input("Enter the absolute name of the file: ")
filemode = input("Enter the mode in which you want to open above file(r, w, x, a): ")


if filemode == 'r':
    print('')
    print("Reading the file content")
    print('')
    print('*' * 30)
    count = 0
    custom_file = open(filename, filemode)
    for line in custom_file:
        count += 1
        print("lineNo: ", count, " - ", line)

    custom_file.close()

elif filemode == 'w':
    print('')
    print("Inserting some content to file")
    custom_file = open(filename, filemode)
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

elif filemode == 'a':

    print('')
    print('*' * 30)
    print('')
    print("Appending some extra lines")
    custom_file = open(filename, filemode)
    extrastring = input("Enter some extra content: ")
    custom_file.write("\n")
    custom_file.write(extrastring)
    custom_file.close()



    print('')
    print("Reading the updated file content")
    count = 0
    custom_file = open(filename, 'r')
    for line in custom_file:
        count += 1
        print("lineNo: ", count, " - ", line)

    custom_file.close()


else:
    print("Exiting Thanks!")