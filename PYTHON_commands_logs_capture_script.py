#!/usr/bin/env python3
import subprocess, os

os.system('echo "Welcome to logs capturing script\n"')

# Defining required variables #

commandfilePath = '/root/codes/commandList.txt'       
logFilePath = input("Enter log file name: ? ")        
errorFilePath = input("Enter Error log file name: ? ")
print("")

# Deleting the files if already present #

for logfile in logFilePath, errorFilePath:

    if os.path.exists(logfile):
        os.remove(logfile)

# Proceeding with logs capturing only when commands file present #

filepresence = input("Is commandList.txt contains commands? (y/n) ")
if filepresence == 'y':

    # Reading all commands and iterating in a list #
    with open(commandfilePath, "r") as f:
        fo = f.readlines()

    new_list = []
    for element in fo:
        new_list.append(element.replace("\n", ""))

    fo = new_list

    # Putting a header entry in required files
    logheader = os.popen('echo "Capturing logs for $HOSTNAME on `date`" > %s ; echo "\n"' % logFilePath, 'w')
    logheader.close()
    errorheader = os.popen('echo "Capturing logs for $HOSTNAME on `date`" > %s ; echo "\n"' % errorFilePath, 'w')
    errorheader.close()
    # Capturing command output in log files and any errors in error file
    for command in fo:
        with open(logFilePath, "a") as outLogFile, open(errorFilePath, "a") as outErrorFile:
            print("=" * 20, command, "=" * 20, file=outLogFile)
            print("=" * 20, command, "=" * 20, file=outErrorFile)
            print("", file=outLogFile)

        with open(logFilePath, "a") as outLogFile, open(errorFilePath, "a") as outErrorFile:
            subprocess.run(command, shell=True, stdout=outLogFile, stderr=outErrorFile)
            print("", file=outLogFile)

# Final output printing declaring closure of script #

os.system('echo "Logs capturing script completed\n"')
print("Command logs file: ", logFilePath)
print("Error logs File: ", errorFilePath)