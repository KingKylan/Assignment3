# manager.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ervin Grimaldi
# egrimal1@uci.edu
# 51767760

from pathlib import Path
import local_handle
import Process_path
import a3
import Profile
first = True
admin = False
profile = Profile.Profile()

class Standard:
    # standard functions
    def __init__(self, path, operations, name):
        self.path = path
        self.operations = operations
        self.name = name
        if len(operations) == 0:
            Standard.listing(self)
        else:
            Standard.standards(self)

    def listing(self):
        p = Path(self.path)
        for file in p.iterdir():
            if file.is_file():
                print(file)
        for dir in p.iterdir():
            if dir.is_dir():
                print(dir)
        run()

    def standards(self):
        p = Path(self.path)
        if '-f' in self.operations:
            for element in p.iterdir():
                if element.is_file():
                    print(element)
        if '-s' in self.operations:
            for element in p.iterdir():
                if element == p / self.name:
                    print(element)
        if '-e' in self.operations:
            for element in p.iterdir():
                if element.suffix == self.name:
                    print(element)
        run()

# class used almos as a folder. Group togheter all reursive options
class Recursive:
    def __init__(self, path, operations, name):
        self.path = path
        self.operations = operations
        self.name = name
        if len(operations) == 1 and '-r' in operations:
            Recursive.recursive(self)
        elif '-f' in operations:
            Recursive.files(self)
        elif '-s' in operations:
            Recursive.Name_same(self)
        elif '-e' in operations:
            Recursive.Ext_same(self)

# backbone of recursive method
    def recursive(self):
        p = Path(self.path) # set path

        # change path to a directory
        def Rec_tree(path):
            p = Path(path)
            Rec(p)
        # separate file and dir, if is a dir, change path to dir's path
        def Rec(p):
            for element in p.iterdir():
                if element.is_file():
                    print(element)
            for element in p.iterdir():
                if element.is_dir():
                    print(element)
                    Rec_tree(element)

        Rec(p)
        run()

    def files(self):
        p = Path(self.path)

        def Rec_tree(path):
            p = Path(path)
            Rec(p)

        def Rec(p):
            for element in p.iterdir():
                if element.is_file():
                    print(element)
            for element in p.iterdir():
                if element.is_dir():
                    Rec_tree(element)

        Rec(p)
        run()

    def Name_same(self):
        p = Path(self.path)

        def Rec_tree(path):
            p = Path(path)
            Rec(p)

        def Rec(p):
            for element in p.iterdir():
                if element.is_file() and element == p / self.name:
                    print(element)
            for element in p.iterdir():
                if element.is_dir():
                    Rec_tree(element)

        Rec(p)
        run()

    # Looks for a file with the same extension in a recursive way
    def Ext_same(self):
        p = Path(self.path)

        def Rec_tree(path):
            p = Path(path)
            Rec(p)

        def Rec(p):
            for element in p.iterdir():
                if element.is_file() and element.suffix == self.name:
                    print(element)
            for element in p.iterdir():
                if element.is_dir():
                    Rec_tree(element)

        Rec(p)
        run()


'''Program backbone. Has the role to check if the initial code is valid, 
if admin mode is active and if user request to exit code'''


def run():
    global first, admin
    a = input()
    if len(a) <= 1 and a != 'Q' and a != 'E' and a != 'P':
        print('ERROR')
        first = False
        run()
    if (len(a) < 3 or a[0] == ' ') and a != 'Q' and a != 'E' and a != 'P':
        print('ERROR')
        first = False
        run()
    elif a == 'Q':
        if not admin:
            print(a3.goodbye)
        quit()
    elif a == 'admin' and first:
        first = False
        admin = True
        run()
    if a == 'join' or a == 'post' or a == 'bio':
        if local_handle.p1 == '':
            print(a3.Path_request)
            check = input()
            if check == 'Q':
                print(a3.goodbye)
                quit()
            elif check == 'y':
                p = input()
                Process_path.DSP_path(p, a)
            else:
                run()
        else:
            print('we do have the path')
            a3.join(local_handle.p1)


    else:
        first = False
        Process_path.process(a, admin)

def server_run(path, a=None):
    if a == 'join':
        temp_name = input('insert name: ')
        temp_pass = input("insert password: ")
        if temp_pass != profile.password or temp_name != profile.username:
            print('INSERT AGAIN. Name and\\or password is incorrect')
            server_run(path, a)
