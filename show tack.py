 ����� ����� netstat ���� ������ �� ����� ������� SSH �� ���� ���
command = f"netstat -tna | grep ':22' | grep 'ESTABLISHED' | awk '{{print $4}}' | awk -F':' '{{print $NF}}' | grep '{target_port}'"
stdin, stdout, stderr = ssh.exec_command(command)

# ������ ����� ����� netstat � ������ ����� ������� SSH ���� ���� ���
output = stdout.readlines()
ssh_count = len(output)

# ����� ����� ������� SSH ���� ���� ���
print(f'{ssh_count} connections on port {target_port}')

# ��� ������ �� ����
ssh.close()