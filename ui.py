# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Ervin Grimaldi
# egrimal1@uci.edu
# 51767760

'''THIS FILE IS INDIPENDENT.'''



menu = f"""
{'WELCOME':^100}
{'='*100}

{'Use Q when selecting options to leave the program':^100}
\n
{'LIST OF OPTIONS:':^100}
L = Return to the user a list of elements in a specified directory
{'ATTENTION':^100}\n{'This command has to be formatted as [COMMAND] [INPUT] [[-]OPTION] [INPUT]':^100}
{'List of options:':^75} \n-r Output directory content recursively.
-f Output only files, excluding directories in the results.
-s Output only files that match a given file name.
-e Output only files that match a give file extension.
\nC = Create a new file in the specified directory.
D = Delete the file.
R = Read the contents of a file
O = Open an existing file of the type dsu
{'ATTENTION':^100}\n{'Those command have to be formatted as [COMMAND] [PATH]':^100}
\n
E = Edit the DSU file loaded by C or O commands
-usr [USERNAME]
-pwd [PASSWORD]
-bio [BIO]
-addpost [NEW POST]
-delpost ["ID"] ATTENTION, The number id must be wrapped between " " as shown. 
\n
P = Print data in the DSU file loaded by C or O commands
-usr Prints the username stored in the profile object
-pwd Prints the password stored in the profile object
-bio Prints the bio stored in the profile object
-posts Prints all posts stored in the profile object with id (using list index is fine)
-post [ID] Prints post identified by ID
-all Prints all content stored in the profile object
{'='*100}
"""

ask_server = 'Server: '
file_dont_exist = "file doesn't exists"
error = 'ERROR'
empty = 'EMPTY'
cancellato = 'DELETED'
file_error = f'ERROR\n selected .dsu do not exists'
loaded = f'{"+" * 90:^20}\n{"+" * 90:^20}\n your .DSU file has been successfully loaded'
file_content = f'\n{"this is your contend in the file":^100} \n'
ask_username = 'Username: '
ask_password = 'Password: '
ask_bio = 'Bio: '
goodbye = 'have a great day!'
error_user_pass = 'ATTENTION, username and\or password cannot have spaces, try again'
exists = 'EXISTS'
Path_request = 'PATH not selected. insert "y" to insert PATH to .dsu profile manually, else press any other ' \
               'combination of characters '
not_path = 'ATTENTION\nPATH not selected, please Run command O or R before to select the .DSU file path'
create_welcome = f"{'='*100}\nDO NOT ADD SPACES FOR USERNAME AND NAME\nYou don't need to open the profile once created!"
welcome_open = f"{'='*100}\nOnce loaded your profile you don't have to do anything else!\n{'='*100}\n"
welcome_edit = f"""{'='*100}\nManual save is not needed. Every change is automatically saved!\nOPTIONS:\n
E = Edit the DSU file loaded by C or O commands
-usr [USERNAME]
-pwd [PASSWORD]
-bio [BIO]
-addpost [NEW POST]
-dellpost ["ID"] ATTENTION, The number id must be wrapped between " " as shown. \n{'='*100}\n"""
welcome_print = f"""{'='*100}\nYour profile won't save or update any element!\nOPTIONS:\n-usr Prints the username stored in the profile object
-pwd Prints the password stored in the profile object
-bio Prints the bio stored in the profile object
-posts Prints all posts stored in the profile object with id (using list index is fine)
-post [ID] Prints post identified by ID
-all Prints all content stored in the profile objectC\n{'='*100}\n"""
welcome_standard = '''-f Output only files, excluding directories in the results.
-s Output only files that match a given file name.
-e Output only files that match a give file extension.\n{'='*100}\n'''
welcome_recursive = '''r Output directory content recursively.
-f Output only files, excluding directories in the results.
-s Output only files that match a given file name.
-e Output only files that match a give file extension.\n{'='*100}\n'''
