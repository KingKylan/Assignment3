# process_path.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Trevor Walker
# walkertk@uci.edu
# 35049080
# Ervin Grimaldi
# egrimal1@uci.edu
# 51767760
from a3 import command
from sys import platform
import local_handle
import manager
import time

# divide and handle path, check the OS of the user and adapt based on it split strings based on the operation that is requested.
def process(string, admin):
    name = ''
    path = ''
    cmd = string[0]
    # TODO WHEN WE ARE ON WINDOWS OS
    if platform == 'win32':
        operations = [i for i in string.split(' ') if '-' in i and '\\' not in i]
        path = [i for i in string.split(' ') if i not in operations][1:]
        path = ' '.join(path)
        if '-s' in operations or '-e' in operations:
            name = ' '.join([i for i in path.split() if '\\' not in i])
            path = [i for i in path.split() if i not in name]
            if '-e' in operations:
                name = f'.{name}'
        else:
            path = [i for i in string.split(' ') if i not in operations][1:]
        path = ' '.join(path)

        if cmd == 'C' or cmd == 'D' or cmd == 'R' or cmd == 'O':
            name = ' '.join([i for i in path.split() if '\\' not in i])
            path = ' '.join([i for i in path.split() if i not in name])

        if cmd == 'E':
            string = string[2:]
            division_str = [i for i in string.split('"') if i != '']
            for i in range(len(division_str)):
                if division_str[i][-1] == ' ' or division_str[i][0] == " ":
                    division_str[i] = division_str[i].strip()
            operations = division_str
        if cmd == 'P':
            string = string[2:]
            operations = [i for i in string.split(" ")]

    # TODO  WHEN IS NOT ON WINDOWS OS
    else:
        print('THIS IS NOT WINDOWS')
        operations = [i for i in string.split(' ') if '-' in i and '/' not in i]
        path = [i for i in string.split(' ') if i not in operations][1:]
        path = ' '.join(path)
        if '-s' in operations or '-e' in operations:
            name = ' '.join([i for i in path.split() if '/' not in i])
            path = ([i for i in path.split() if i not in name])
            if '-e' in operations:
                name = f'.{name}'
        else:
            path = [i for i in string.split(' ') if i not in operations][1:]
        path = ' '.join(path)
        if cmd == 'C' or cmd == 'D' or cmd == 'R':
            name = ' '.join([i for i in path.split() if '/' not in i])
            path = ' '.join([i for i in path.split() if i not in name])

        if cmd == 'E':
            string = string[2:]
            division_str = [i for i in string.split('"') if i != '']
            for i in range(len(division_str)):
                if division_str[i][-1] == ' ' or division_str[i][0] == " ":
                    division_str[i] = division_str[i].strip()
            operations = division_str
        if cmd == 'P':
            string = string[2:]
            operations = [i for i in string.split(" ")]
    command(cmd, path, operations, name, admin)
    
    
# Deals with handeling the path and input to put it in a usable format.
def DSP_path(p, a):
    if platform == 'win32':
        name_file = [i for i in p.split(' ') if '\\' not in i]
        path = ' '.join([i for i in p.split() if i not in name_file])
        name_file = ' '.join(name_file)
        if len(name_file) == 0:
            print('EXISTS')
            flag = True
            local_handle.open(path, name_file, flag)
            pass
        else:
            print('WE CREATE')
            flag = True
            local_handle.create(path, name_file, flag)
        manager.server_run(p, a)
    else:
        name_file = [i for i in p.split(' ') if '/' not in i]
        path = ' '.join([i for i in p.split() if i not in name_file])
        name_file = ' '.join(name_file)

