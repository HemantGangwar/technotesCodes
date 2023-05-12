#!/usr/bin/env python3

import subprocess
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', action='store_true', required=False, dest='count')
parser.add_argument('--list', action='store_true', required=False, dest='list')
parser.add_argument('--list-hosts', action='store_true', required=False, dest='listhost')
args = parser.parse_args()

bash_out = subprocess.Popen("aws ec2 describe-instances --query 'Reservations[*].Instances[*].PublicIpAddress' --output text", shell=True, stdout=subprocess.PIPE).stdout.read()

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

if '\\n' in bash_out_deco:
    bash_out_list = bash_out_deco.split('\\n')
else:
    bash_out_list = bash_out_deco.split('\n')


server_list = []
server_list = bash_out_list

# Handling exceptions

try:
    server_list.remove('')
except ValueError:
    pass

for server in server_list:
    servers['mygroup']['hosts'].append(server)

if args.list:
    print(json.dumps(servers))
elif args.listhost:
    print(json.dumps(servers))
else:
    print(len(servers['mygroup']['hosts']))
