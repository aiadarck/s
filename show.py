import os
import uuid
import random
import subprocess

tl_path = os.popen('which tl').read().strip()

domain = 'meta.consolcbr.xyz'

uuid_val = str(uuid.uuid4())

port = random.randint(1025, 65535)

config_path = os.path.join(os.getcwd(), f'{domain}.json')

tl_command = [tl_path, 'full', 'client', f'--url=ws://{domain}:{port}', '--type=vless', '--security=tls', f'--uuid={uuid_val}', '--mux=0']
with open(config_path, 'w') as config_file:
    subprocess.run(tl_command, stdout=config_file)

print(f'VLESS config created for domain {domain} with UUID {uuid_val} and port {port}: {config_path}')

qemu_path = os.popen('which qemu-img').read().strip()

disk_size_mb = 20000

qemu_command = [qemu_path, 'create', '-f', 'qcow2', 'user.qcow2', f'{disk_size_mb}M']
subprocess.run(qemu_command)

print(f'Disk image created for user with size {disk_size_mb} MB: user.qcow2')
