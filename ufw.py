import paramiko

command = "sudo ufw enable"
stdin, stdout, stderr = ssh_client.exec_command(command)
print(stdout.read().decode())

# œ—ŒÊ«”  Ê—Êœ ÅÊ—  Â«
ports = []
num_ports = int(input("Enter the number of ports to allow: "))
for i in range(num_ports):
    port = input(f"Enter port {i+1}: ")
    ports.append(port)

# Ê«—œ ò—œ‰ ÅÊ—  Â« œ— ›«Ì—Ê«·
for port in ports:
    command = f"sudo ufw allow {port}"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    print(stdout.read().decode())

# –ŒÌ—Â ÅÊ—  Â« œ— ›«Ì·
with open("allowed_ports.txt", "w") as f:
    for port in ports:
        f.write(port + "\n")

# ﬁÿ⁄ «— »«ÿ SSH
ssh_client.close()