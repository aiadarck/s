python
import os


port = input('Enter the port number: ')


command = f"netstat -tna | grep ':{port}' | grep 'ESTABLISHED' | awk '{{print $4}}' | awk -F':' '{{print $NF}}'"
output = os.popen(command).read()

ssh_count = {}
for p in output.split():
    if p in ssh_count:
        ssh_count[p] += 1
    else:
        ssh_count[p] = 1

for p, count in ssh_count.items():
    print(f'Port {p}: {count} connections')