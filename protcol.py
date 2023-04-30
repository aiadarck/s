import urllib.request
import random
import string

# Generate random X-ui URL, username and password
xui_url = 'meta.consolcbr.xyz'
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

# Generate random port between 1024 and 65535
port = random.randint(1024, 65535)

# Generate random username with length 8
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

# Create new VLESS account with WebSocket and TLS protocol
create_account_url=f'{xui_url}/api/v1/create?type=vless&net=ws&t="ws"&tls=true&port={port}&user={username}'
response = urllib.request.urlopen(create_account_url)
account_info = eval(response.read())

# Generate URL from account info
vless_url = f"vless://{account_info['id']}@{account_info['add']}:{account_info['port']}?encryption={account_info['aid']}&security=tls&sni={account_info['add']}&type=ws&path=%2f{account_info['path']}#Avash-%D8%AA%D8%A7%D9%86%D9%84-4nv6sf"

# Print VLESS URL
print(vless_url)