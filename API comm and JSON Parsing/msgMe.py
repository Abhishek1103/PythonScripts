acc = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

myNumber = "+XXXXXXXXXX"
twilioNumber = "+XXXXXXXXXX"

from twilio.rest import Client

def textme(message):
    client = Client(acc,token)
    client.messages.create(to=myNumber, from_=twilioNumber, body=message)


message = "My first twilio message....COOL.."
textme(message) 
