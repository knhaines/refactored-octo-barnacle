# scp_transfer.py

import paramiko
import sys

# Get SSH parameters from command-line arguments
hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
local_file = sys.argv[4]
remote_file = sys.argv[5]

# SCP transfer
try:
    # Create an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote server
    ssh.connect(hostname, username=username, password=password)

    # SCP transfer
    scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    scp.put(local_file, remote_file)

    print(f"File {local_file} successfully transferred to {remote_file} on {hostname}")
    scp.close()
    ssh.close()

except Exception as e:
    print(f"Error during SCP transfer: {e}")
