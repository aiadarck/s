
#!/bin/sh

if [ "$(id -u)" != "0" ]; then
	echo "You must be root to execute the script. Exiting."
	exit 1
fi

if [[ -z "${1}" ]]; then
  echo "Please run the script with a port at the end. Like 9011 "
  exit 1 
fi
public_address=$(curl -s checkip.amazonaws.com )

semanage port -a -t ssh_port_t -p tcp $1 > /dev/null 2>&1
sed -i -e "/Port /c\Port $1" /etc/ssh/sshd_config
service sshd restart  > /dev/null 2>&1
firewall-cmd --zone=public --add-port=$1/tcp --permanent  > /dev/null 2>&1
sudo iptables -I INPUT -p tcp -m tcp --dport $1 -j ACCEPT  > /dev/null 2>&1
iptables-save > /etc/sysconfig/iptables  > /dev/null 2>&1
clear 
echo "$(tput setaf 2)"Your SSH port was changed to $1. Good luck "$(tput sgr0)"
echo "$(tput setaf 3)"New Access / ssh root@$public_address -p $1"$(tput sgr0)"


