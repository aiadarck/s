import os
import re
import paramiko


target_port = input('Enter the port to check: ')

command = f"netstat -tna | grep ':22' | grep 'ESTABLISHED' | awk '{{print $4}}' | awk -F':' '{{print $NF}}' | grep '{target_port}'"
stdin, stdout, stderr = ssh.exec_command(command)


output = stdout.readlines()
ssh_count = len(output)


print(f'{ssh_count} connections on port {target_port}')