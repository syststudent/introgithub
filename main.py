import subprocess
import os

print('/help - get available commands,\npath - current path,\nredirect [path] - redirect to path,\nexit - exit program')
while True:
    command = input('>').split(' ')
    if command[0] == 'path':
        subprocess.run('cd', shell=True)
    elif command[0] == 'redirect':
        os.chdir(command[1])
    elif command[0] == '/help':
        print('/help - get available commands,\npath - current path,\nredirect [path] - redirect to path,\nexit - exit program')
    elif command[0] == 'exit':
        break
    else:
        print('unknown command')
