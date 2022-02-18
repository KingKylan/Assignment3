# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Trevor Walker
# walkertk@uci.edu
# 35049080

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port))
    print("client connected to {server} on {port}")
    
    # need to figure out how to put into JSON object here probably best to create a file with a2 stuff because it stores it in json format
    # json_message = json(message)
    
    clinet.sendall(json_message)
    
  '''
  The send function joins a ds server and sends a message, bio, or both
  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  return 
