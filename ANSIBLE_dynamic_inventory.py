#!/usr/bin/env python3
# Author: Hemant Gangwar
# Description: Dynamic inventory for python 3 based systems
# Data pick location: This script will dynamic find the hostlist from the /etc/hosts on Linux based systems.
# Contacts: learningtechnix@gmail.com

import subprocess
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', action='store_true', required=False, dest='count')
parser.add_argument('--list', action='store_true', required=False, dest='list')
args = parser.parse_args()

bash_out = subprocess.Popen("cat /etc/hosts | grep -v localhost | grep -v '#' | grep -v ^$ | awk '{print $2}' | cut -d'.' -f1", shell=True, stdout=subprocess.PIPE).stdout.read()

bash_out_deco = bash_out.decode()

servers = {
    "_meta": {
        "hostvars": {}
  },
    "mygroup": {
        "hosts": []
    },
    "local": {
        "hosts": ["127.0.0.1"]
    }
}

# Added some logic to account for newer versions of Ansible formatting newlines differently
if '\\n' in bash_out_deco:
    bash_out_list = bash_out_deco.split('\\n')
else:
    bash_out_list = bash_out_deco.split('\n')

#bash_out_list = str(bash_out).split('\n')

server_list = []
server_list = bash_out_list
#for line in bash_out_list:
#    server_list.append(line.replace('\'', '').replace("b", ''))
#server_list.append(bash_out_list)

# exception catch in case there aren't any empty lines
try:
    server_list.remove('')
except ValueError:
    pass

for server in server_list:
    servers['mygroup']['hosts'].append(server)

if args.list:
#    print(json.dumps(servers))
     print(json.dumps(servers))
else:
    print(len(servers['mygroup']['hosts']))