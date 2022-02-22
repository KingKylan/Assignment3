# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Trevor walker
# walkertk@uci.edu
# 35049080
# Ervin Grimaldi
# egrimal1@uci.edu
# 51767760


from Profile import Profile, Post
from ui import *
import manager
import local_handle


'''
PROGRAM OUTILINE-MAP
(a3 <-> ui)     #This is where the program starts. When started, direct to run function in manager.py
    | |
   manager [run]    #here the user-command input is taken and tested the validity. Once valid the command is processed
    | |
   Process_Path     #The input get splited in minor section and used for comands. Splits occurs through a combination of 
    | | 
   local_handle     #Journal's function resides here. This file has the role of managing the user's Profile and give the change to post online or save only localy
'''


# This function riderect the user input to the proper function
def command(cmd, path, operations, name='', servo=False):   # cmd is the command, path is the path to the local .dsu file, operations are the set of commands for the visualization of local file managment, name is the name of the file that the user want to create
    global admin    # delcare globally admin, useful for UI. Servo has the role to check if admin mode is active or not
    admin = servo

    dict = {'-usr': '', '-bio': '', '-pwd': '', '-posts': '', '-post': '', '-addpost': [], '-delpost': ''}  #set to empty the values. This allow to not create duplicate and let the function work
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

    else:
        print(error)
        manager.run()   # In case of error, Loop back for new user's input


# Program begins
if __name__ == '__main__':
    print(menu)
    manager.run()   # Direct to a function run, which manage the initial input and is the backbone of the program
