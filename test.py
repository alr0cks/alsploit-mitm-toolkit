import subprocess
all_interface = subprocess.check_output(["nmcli", "device", "status"]).decode('utf-8')
print(all_interface)