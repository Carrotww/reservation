import os
from twilio.rest import Client
from dotenv import load_dotenv


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

load_dotenv()
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
server_phone_number = os.environ.get('SERVER_PHONE_NUMBER')
phone_number_1 = os.environ.get('TARGET_PHONE_NUMBER_MY')
phone_number_2 = os.environ.get('TARGET_PHONE_NUMBER_SE')

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="",
                     from_=server_phone_number,
                     to=phone_number_1
                 )