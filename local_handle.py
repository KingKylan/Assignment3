from pathlib import Path
from os import remove
import a3
import manager
from Profile import Profile, Post

profile1 = Profile()
post = Post()
flag = False
p1 = ''
p = ''
first = True

'''This function created the .dsu file, ask for basic user information and declare globally the path <=> user profile'''


def create(path, name, flag_dsu=False):
    global p1
    p = Path(path)
    p1 = p / f'{name}.dsu'
    if not p1.exists():
        if not manager.admin:
            print(a3.create_welcome)
        p1.touch()
        username = input(a3.ask_username)
        if ' ' in username:
            print(a3.error_user_pass)
            remove(p1)
            create(path, name)

        password = input(a3.ask_password)
        if ' ' in password:
            print(a3.error_user_pass)
            remove(p1)
            create(path, name)
        bio = input(a3.ask_bio)

        profile1.username, profile1.password, profile1.bio, profile1._posts = username, password, bio, []  # save user's informations
        Profile.save_profile(profile1, p1)
        if manager.admin == False:
            print(a3.loaded)
            print('File path: ', p1)
    else:
        if manager.admin == False:
            print(a3.exists)
        pass
    if not flag_dsu:
        manager.run()
    else:
        pass

# Load profile given the path precedently took. Profile do not get saved to avoid duplicates
def open(path, name, flag_dsu=False):
    global p1, p
    lista = []
    p1 = Path(path)
    if not p1.exists() or not p1.suffix == '.dsu':
        if not manager.admin:
            print(a3.file_error)
        manager.run()
    elif p1.exists():
        if manager.admin == False:
            print(a3.welcome_open)
        if p != p1:
            p = p1
            profile1._posts = []  # avoid that two users posts overlaps
            profile1.load_profile(p1)
        # Profile.save_profile(profile1, p1)
        f = p1.open()
        if not manager.admin:
            print(a3.loaded)
        print(a3.file_content)
        for i, line in enumerate(f.readlines()):  # read all posts and print them
            lista.append(line)
            if lista[i] == lista[-1]:
                lista[i] = lista[i][:-1]
        for element in lista:
            print(element)
    else:
        print(a3.error)
    if not flag_dsu:
        manager.run()
    else:
        pass

# delete a file
def dell(path, name):
    p = Path(path)
    p1 = p / name

    if not p1.exists():
        print()
        pass
    else:
        print(f'{p1} DELETED')
        remove(p1)
    manager.run()


# read the file, user is not saved and not uploaded
def read(path, name):
    lista = []
    p1 = Path(path)
    if not p1.exists() or not p1.suffix == '.dsu':
        print(a3.error)
        manager.run()
    elif p1.exists():
        f = p1.open()
        if p1.stat().st_size == 0:
            print(a3.empty)
        else:
            for i, line in enumerate(f.readlines()):
                lista.append(line)
                if lista[i] == lista[-1]:
                    lista[i] = lista[i][:-1]
            for element in lista:
                print(element)
    else:
        print(a3.error)
    manager.run()


# user is precedently uploaded, here the file is saved every since interaction
# post use a list to enable different posts entry in a time
# a dicotonary is used to store the element inputed by the user, afterwards is saved in profile
def edit(operations, dict):
    if not manager.admin:
        print(a3.welcome_open)
    if p1 == '':
        if not manager.admin:
            print(a3.not_path)
        manager.run()
    else:
        for i, element in enumerate(operations):
            if element in dict.keys():
                if element == '-addpost':
                    dict[element].append(operations[i + 1])
                else:
                    dict[element] = operations[i + 1]
        if dict['-usr'] != '':
            profile1.username = dict['-usr']
        if dict['-bio'] != '':
            profile1.bio = dict['-bio']
        if dict['-pwd'] != '':
            profile1.password = dict['-pwd']
        if dict['-addpost'] != '':
            for element in dict['-addpost']:
                post = Post(element)
                profile1.add_post(post)
        if dict['-delpost'] != '':
            profile1.del_post(int(dict['-delpost']) - 1)
        profile1.save_profile(p1)

    manager.run()


# profile is just printed, not saved
def output_print(operations, dict):
    if p1 == '':
        if not manager.admin:
            print(a3.not_path)
        manager.run()
    else:
        if not manager.admin:
            print(a3.welcome_print)
        lista_opt = ['-usr', '-pwd', '-bio', '-posts', '-post', '-all', '-post']
        for element in operations:
            if element in lista_opt:
                if element == '-usr':
                    print(f'USERNAME: {profile1.username}')
                if element == '-pwd':
                    print(f'PASSWORD: {profile1.password}')
                if element == "-bio":
                    print(f'BIO: {profile1.bio}')
                if element == '-posts':
                    for i, element in enumerate(profile1.get_posts()):
                        print(f'ID: {i + 1} {element.entry}')

                if element == '-post':
                    index = operations[operations.index(element) + 1]
                    if '"' in index:
                        index = index.strip('"')
                    elif "'" in index:
                        index = index.strip("'")
                    else:
                        pass
                    index = int(index)
                    for i, element in enumerate(profile1.get_posts()):
                        if i + 1 == index:
                            print(f'POST AT ID {index}: {element.entry}')
                if element == '-all':
                    print(f'USERNAME: {profile1.username}\n'
                          f'PASSWORD: {profile1.password}\n'
                          f'BIO: {profile1.bio}\n'
                          f'POSTS:', end='')
                    print()

                    for i, element in enumerate(profile1.get_posts()):
                        print(f'{i + 1}, {element.entry} at {element.timestamp}', end=' ')

    manager.run()
