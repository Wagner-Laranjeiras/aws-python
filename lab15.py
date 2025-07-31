import os
import subprocess

# Task 1
print('Task one:')
os.system('ls')

# Task 2 - 4
print('Task two to four: ')
# subprocess.run(['ls'])
# subprocess.run(['ls', '-l'])
subprocess.run(['ls', '-l', 'python.py'])

# Task 5
print('Task five: ')
command='uname'
commandArgument='-a'
print(f'Gathering sys info with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Task 6
print('Task six')
command='df'
commandArgument='-h'
print(f'Gathering active process info with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])


