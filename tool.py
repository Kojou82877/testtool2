import time
from fbchat import Client
from fbchat.models import *

# Get the user's Facebook login credentials
username = input('Enter your Facebook email: ')
password = input('Enter your Facebook password: ')

# Get the ID of the user or group to send the message to
target_id = input('Enter the ID of the user or group you want to send the message to: ')

# Get the message to send
message = input('Enter the message you want to send: ')

# Get the time delay for the next message in seconds
delay = int(input('Enter the time delay between messages (in seconds): '))

# Log in to Facebook
client = Client(username, password)

# Send the message
client.send(Message(text=message), thread_id=target_id, thread_type=ThreadType.USER)

# Wait for the specified time delay
time.sleep(delay)

# Log out of Facebook
client.logout()
