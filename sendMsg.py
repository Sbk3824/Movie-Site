import twilio

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACe3ee3300d1ef3c97578cb7c59387e1fa'
auth_token = '01f7e8dc1a57dac115110fb41214fe4f'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hey Man!',
                              from_='+18303553824',
                              to='+16692120142'
                          )

print(message.sid)

