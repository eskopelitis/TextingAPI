from twilio.rest import Client
from creds import account_sid, auth_token 

client = Client(account_sid, auth_token)

my_cell = input('Who do you want to text?: ')
my_message = input('What do you want to say: ')

message = client.messages.create(         
                              to=my_cell, from_ = '+18456608147', body = my_message
                          ) 
 
print(message.sid)