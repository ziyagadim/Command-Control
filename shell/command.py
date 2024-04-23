import subprocess

result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE)
print(result.stdout.decode())