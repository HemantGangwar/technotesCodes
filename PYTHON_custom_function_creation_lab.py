#!/usr/bin/env python
import os, subprocess

def welcome_banner(note):
    """ This is print custom message of choice """
    print('')
    print(note)
    print('*' * 30)
    print('')

def logs_variable_define():
    logFile = input("Enter log file name: ? ")
    errorFile = input("Enter Error log file name: ? ")
    for logfile in logFile, errorFile:
        if os.path.exists(logfile):
            os.remove(logfile)
    logheader = os.popen('echo "Capturing logs for $HOSTNAME on `date`" > %s ; echo "\n"' % logFile, 'w')
    logheader.close()
    errorheader = os.popen('echo "Capturing logs for $HOSTNAME on `date`" > %s ; echo "\n"' % errorFile, 'w')
    errorheader.close()
    return logFile, errorFile


def my_custom_func(*commands):
    """ This is for passing series of commands to capture the outputs """
    logFilePath, errorFilePath = logs_variable_define()
    for command in commands:
        with open(logFilePath, "a") as outLogFile, open(errorFilePath, "a") as outErrorFile:
            print("=" * 20, command, "=" * 20, file=outLogFile)
            print("=" * 20, command, "=" * 20, file=outErrorFile)
            print("", file=outLogFile)

        with open(logFilePath, "a") as outLogFile, open(errorFilePath, "a") as outErrorFile:
            subprocess.run(command, shell=True, stdout=outLogFile, stderr=outErrorFile)
            print("", file=outLogFile)


welcome_banner('Welcome to logs capturing script')
my_custom_func('uname -a', 'df -h', 'uptime', 'ansible -v', 'ip -4 a')
welcome_banner('Logs capturing script completed')