 ÇÌÑÇí ÏÓÊæÑ netstat ÈÑÇí ÏÓÊÑÓí Èå ÊÚÏÇÏ ÇÊÕÇáÇÊ SSH ÏÑ æÑÊ ÎÇÕ
command = f"netstat -tna | grep ':22' | grep 'ESTABLISHED' | awk '{{print $4}}' | awk -F':' '{{print $NF}}' | grep '{target_port}'"
stdin, stdout, stderr = ssh.exec_command(command)

# ÎæÇäÏä ÎÑæÌí ÏÓÊæÑ netstat æ ãÍÇÓÈå ÊÚÏÇÏ ÇÊÕÇáÇÊ SSH ÈÑÇí æÑÊ ÎÇÕ
output = stdout.readlines()
ssh_count = len(output)

# äãÇíÔ ÊÚÏÇÏ ÇÊÕÇáÇÊ SSH ÈÑÇí æÑÊ ÎÇÕ
print(f'{ssh_count} connections on port {target_port}')

# ŞØÚ ÇÑÊÈÇØ ÈÇ ÓÑæÑ
ssh.close()