import subprocess
cmd = ['ping', '-c', '3', '8.8.8.8']
shell_cmd = subprocess.run((cmd))
