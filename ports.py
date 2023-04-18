import paramiko

# Get user input for the new port number
new_port = input("Please enter a new port number: ")

# Open the sshd_config file and update the port number
stdin, stdout, stderr = ssh.exec_command('sudo nano /etc/ssh/sshd_config')
stdin.write('\nPort {}\n'.format(new_port))
stdin.flush()
stdin.write('\x01')  # Send Ctrl+A to select all text
stdin.write('\x06')  # Send Ctrl+F to search for text
stdin.flush()
stdin.write('Port ')
stdin.flush()
stdin.write('\x07')  # Send Ctrl+G to find next occurrence of text
stdin.flush()
stdin.write('\x1b')  # Send Esc to exit search mode
stdin.flush()
stdin.write('\x01')  # Send Ctrl+A to select all text again
stdin.flush()
stdin.write('\x16')  # Send Ctrl+V to paste the new port number
stdin.flush()
stdin.write('\x01')  # Send Ctrl+A to select all text again
stdin.flush()
stdin.write('\x15')  # Send Ctrl+U to delete the old port number
stdin.flush()
stdin.write('\n')   # Send Enter to save the file
stdin.flush()

# Get confirmation message and close SSH connection
output = stdout.read().decode('utf-8')
if 'Authentication token manipulation' in output:
    print('Incorrect sudo password entered.')
else:
    print('SSH port updated successfully!')
ssh.close()