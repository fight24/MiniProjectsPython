from twilio.rest import Client
from Key_Api import Key_Api
class Twilio_Class():

    def __init__(self, account_sid = Key_Api['ACC_ID'].value, auth_token = Key_Api['KEY_TWILIO'].value):
        self.__client = Client(account_sid, auth_token)
        self.__message = None

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, body ):
        self.__message = self.__client.messages.create(
                from_=Key_Api['NUM_PHONE'].value,
                body=body,
                to=Key_Api['MY_NUM'].value
                )
    
    @property
    def status(self):
        return self.__message.status
    @property
    def sid(self):
        return self.__message.sid