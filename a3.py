# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ervin Grimaldi
# egrimal1@uci.edu
# 51767760


from Profile import Profile, Post
from ui import *
import manager
import local_handle

def join(p):
    print('QUESTA')
    print(p)
    nome = local_handle.profile1.username
    print(nome)

# This function riderect the user input to the proper function
def command(cmd, path, operations, name='', servo=False):
    global admin    #delcare globally admin, useful for UI
    admin = servo

    dict = {'-usr': '', '-bio': '', '-pwd': '', '-posts': '', '-post': '', '-addpost': [], '-delpost': ''}  #set to empty the values
    if cmd == 'L':
        if '-r' not in operations:
            if not admin:
                print(welcome_standard)
            manager.Standard(path, operations, name)
        else:
            if not admin:
                print(welcome_recursive)
            manager.Recursive(path, operations, name)
    elif cmd == 'C':
        local_handle.create(path, name)
    elif cmd == 'D':
        local_handle.dell(path, name)
    elif cmd == 'R':
        local_handle.read(path, name)
    elif cmd == 'O':
        local_handle.open(path, name)
    elif cmd == 'E':
        local_handle.edit(operations, dict)
    elif cmd == 'P':
        local_handle.output_print(operations, dict)
    elif cmd == 'join':
        join(path)
    else:
        print(error)
        manager.run()


# Program begins
if __name__ == '__main__':
    print(menu)
    manager.run()   # Direct to a function ru, which manage the initial input and is the backbone of the program
