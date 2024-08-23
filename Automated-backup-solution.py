import os
import subprocess
import datetime

def backup_directory(source_directory, remote_user, remote_host, remote_directory):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"backup_{timestamp}.log"


    command = [
        "rsync",
        "-avz", 
        source_directory,
        f"{remote_user}@{remote_host}:{remote_directory}"
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        with open(backup_file, 'w') as f:
            f.write(f"Backup successful:\n{result.stdout}\n")
        print("Backup completedCheck the log:", backup_file)

    except subprocess.CalledProcessError as e:
        with open(backup_file, 'w') as f:
            f.write(f"Backup failed:\n{e.stderr}\n")
        print("Backup failed! Check the log:", backup_file)

source_directory = "/home/user01/bak_files"
remote_user = "testuser"
remote_host = "203.0.113.0"
remote_directory = "/home/elite/bak" 

backup_directory(source_directory, remote_user, remote_host, remote_directory)
