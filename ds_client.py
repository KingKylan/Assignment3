# Trevor Walker
# walkertk@uci.edu
# 35049080
import socket
import json
from collections import namedtuple
from Profile import Profile, Post
import ds_protocol
user_token = ''
current_user = 0
current_pass = 0


# sends the information to the server an makes the post or updates bio if needed and returns False is it fails to 
# properly upload the data

def server_send(request, username, password, token, client):
    # oins the local computer to the server if the requested action was to just join
    if request == 'join':
        try:

            join_msg = '{"join": {"username": "' + username + '", "password": "' + password + '", "token": "' + token + '"}}'

            send = client.makefile('w')
            recv = client.makefile('r')

            send.write(join_msg + '\r\n')
            send.flush()
            response = recv.readline()
        except:
            return False
    # post the user's post to the website if there is a post and returns False is it cant upload the post
    if request == 'post':
        try:
            post_message = '{"token": "' + token + '", "post": {"entry": "' + username + '", "timestamp": "1603167689.3928561"}}'
            send = client.makefile('w')
            recv = client.makefile('r')

            send.write(post_message + '\r\n')
            send.flush()

            response = recv.readline()
        except:
            return False
    # updates the bio to the new bio for the user if the user had requested to change bio
    if request == 'bio':
        try:

            bio_message = '{"token": "' + token + '", "bio": {"entry": "' + username + '", "timestamp": ""}}'
            send = client.makefile('w')
            recv = client.makefile('r')

            send.write(bio_message + '\r\n')
            send.flush()

            response = recv.readline()
        except:
            return False
    # takes the server response and extracts it from json and prints out the message that the server sends as a response
    message = ds_protocol.extract_json(response)
    if message.type == 'ok':
        print(message.message)
        global user_token
        if message.token != '':
            user_token = message.token
        return True
    elif message.type == 'error':
        print(message.message)
        return False


# main send program of the code. Will take the input as the 6 different paramaters and determine what the user wants to 
# do and will appropriately send the server_send function the correct information to upload.
# this serves as the translator between the ui and the actually sending function of server_send.
def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        #tries to connect to the server provided using the port and server ip.
        try:
            client.settimeout(10)
            client.connect((server, port))
        except:
            print('Connection has been refused, Please check IP address and try again')
            return False
        print(f"client connected to {server} on {port}")
        global current_user
        global current_pass
        # checks to see if a different user is trying to connect and if it is a new user updates variables 
        if username != current_user:
            current_user = username
            current_pass = password
            response = server_send('join', username,password,user_token, client)
        # checks to make sure the username and password are correct
        if username == current_user and password != current_pass:
            print('Invalid username or password')
            return False
        # determines what the user wants to do and sends the info to server_send
        if user_token == '':
            current_user = username
            response = server_send('join', username,password,user_token, client)

        if message != '':
            response = server_send('post',message, password, user_token, client)
        if bio != '':
            response = server_send('bio', bio, password, user_token, client)
    # if something fails it will return False 
    if response == False:
        return False
    return True
