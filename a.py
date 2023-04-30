import re

# Open the auth.log file and read it line by line
with open('/var/log/auth.log', 'r') as f:
    content = f.readlines()

# Search for lines containing "Failed password"
failed_password_lines = [line for line in content if "Failed password" in line]

# Extract the IP addresses from each failed password line using regex
ip_addresses = []
for line in failed_password_lines:
    match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if match:
        ip_addresses.append(match.group(0))

# Count the occurrences of each IP address
ip_address_counts = {}
for ip in ip_addresses:
    if ip in ip_address_counts:
        ip_address_counts[ip] += 1
    else:
        ip_address_counts[ip] = 1

# Print the IP addresses and their counts in descending order
for ip, count in sorted(ip_address_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{count} login attempts from {ip}")