import os
import uuid
import random

tl_path = os.popen('which tl').read().strip()

domain = 'meta.consolcbr.xyz'

uuid_val = str(uuid.uuid4())

port = random.randint(1025, 65535)

config_path = os.path.join(os.getcwd(), f'{domain}.json')

tl_command = f'{tl_path} client --url ws://{domain}:{port} --type vless --security tls --uuid {uuid_val} --mux 0 > {config_path}'
os.system(tl_command)

