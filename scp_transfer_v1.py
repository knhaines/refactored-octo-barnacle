#!/usr/bin/env python3
import paramiko
from scp import SCPClient

# Parameters
hostname = '172.16.6.55'
port = 22
username = 'admin'
password = 'WWTwwt1!'  # Replace with the password for 'admin'
local_file = '/home/serverlocal/cisco_iosxe/images/c3560-ipbasek9-mz.150-2.SE11.bin'
remote_path = 'flash:/c3560-ipbasek9-mz.150-2.SE11.bin'

# Set up SSH client and SCP
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Transfer file using SCP
scp = SCPClient(ssh.get_transport())
scp.put(local_file, remote_path)

# Close the SCP session
scp.close()
