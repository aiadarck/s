import os
import uuid
import random

tl_path = '/usr/local/bin/tl'

domain = 'meta.consolcbr.xyz'

uuid_val = str(uuid.uuid4())

port = random.randint(1025, 65535)

config_path = os.path.join(os.getcwd(), f'{domain}.json')

tl_command = f'{tl_path} full client --url ws://{domain}:{port} --type vless --security tls --uuid {uuid_val} --mux 0 > {config_path}'
os.system(tl_command)

print(f'VLESS config created for domain {domain} with UUID {uuid_val} and port {port}: {config_path}')

qemu_path = '/usr/bin/qemu-img'

disk_size_mb = 20000

qemu_command = f'{qemu_path} create -f qcow2 user.qcow2 {disk_size_mb}M'
os.system(qemu_command)

print(f'Disk image created for user with size {disk_size_mb} MB: user.qcow2')
