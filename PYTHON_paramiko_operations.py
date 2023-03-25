#!/usr/bin/env python3

# Importing required Libraries
import shutup;shutup.please()
import paramiko, os, getpass,argparse

# Create the parser
documentation = argparse.ArgumentParser(description='Logs capture mechanism from one or more servers. Choose from one of the below options to perform your operations')
documentation.add_argument("filename", type=str, help="[MANDATORY] file containing the hostlist")
args = documentation.parse_args()
# Close the parser

''' Defining commands whose output you want to capture '''

commands = [
    "uname -a",
    "df -h",
    "date",
    "cat /etc/motd",
    "/usr/sbin/vmtoolsd -v",
    "/usr/bin/vmware-toolbox-cmd -v",
    "cat /etc/fstab",
    "uname -r",
    "cat /etc/redhat-release",
    "lsblk",
    "/sbin/ip -4 a",
    "/opt/VRTS/sbin/hastatus -sum",
    "/sbin/pvs",
    "/sbin/vgs",
    "/sbin/lvs",
    "/sbin/fdisk -l",
    "/sbin/ifconfig -a",
    "/bin/netstat -tulpn | wc -l",
    "/sbin/multipath -ll",
    "/bin/netstat -tulpn",
    "/bin/netstat -rn",
    "/bin/ps -ef | grep -i java",
    "/bin/ps -ef | grep -i java | wc -l",
    "/bin/ps -ef",
    "/usr/sbin/dmidecode |grep -i prod",
]

''' Defining user variables '''
ssh_user  = input('Enter UserName: ')
ssh_password = getpass.getpass()
ssh_port = 22

''' Setting up paramiko for connecting to remote hosts '''

python_ssh_client = paramiko.SSHClient()
python_ssh_client.load_system_host_keys()

with open(args.filename,"r+") as serverlist:
        for server_entry in serverlist.readlines():
                python_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                temphost = server_entry.strip()
                print(f"\n{'='*50}\n Connecting to {temphost}\n{'='*50}")

                # Deleting if log files are present from previous run
                stdOutFile = "%s-logs.txt"%temphost
                stdErrFile = "%s-errorFile.txt"%temphost
                for lastRunFile in stdOutFile, stdErrFile:
                        if os.path.exists(lastRunFile):
                                os.remove(lastRunFile)

                # Handling the servers which are not reachable #

                try:
                        python_ssh_client.connect(temphost, port=ssh_port, username=ssh_user, password=ssh_password)
                except:
                        temp1=open("nodes_unreachable.txt","w")
                        temp1.write("[!] Cannot connect to the SSH Server " + server_entry +"\n")
                        temp1.close()
                        print("[!] Cannot connect to the SSH Server " + server_entry )
                else:
                        # Creating for loop to traverse over commands list #
                        for command in commands:
                                with open("%s-logs.txt"%temphost, "a",encoding="utf-8") as outLogFile, open("%s-errorFile.txt"%temphost, "a", encoding="utf-8") as outErrorFile:
                                        print("=" * 20, command, "=" * 20, file=outLogFile)
                                        print("=" * 20, command, "=" * 20, file=outErrorFile)
                                        print("", file=outLogFile)

                                with open("%s-logs.txt"%temphost, "a", encoding="utf-8") as outLogFile, open("%s-errorFile.txt"%temphost, "a", encoding="utf-8") as outErrorFile:
                                        stdin, stdout, stderr = python_ssh_client.exec_command(command)
                                        for line in (stdout):
                                                outLogFile.write(str(line))
                                        for lineerror in (stderr):
                                                outErrorFile.write(str(lineerror))


serverlist.close()
python_ssh_client.close()
