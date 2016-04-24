from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException

#file = open('ACCSIDAPIKEY.txt', 'r')
##ACCOUNT_SID= file.read()
#file = open('AuthToken.txt', 'r')
##AUTH_TOKEN= file.read()
#file = open('TwilioNumber.txt', 'r')
#FROM_NUM= file.read()


def send_Twilio( TO_NUM, MSG ):
	print "What up"
	client = TwilioRestClient('ACf3776465d6c5eae31fa99d960504d041', 'c111c7fee6d2a14fb6ad031e26f81984')

        try:
	    message = client.messages.create(
	        to = TO_NUM, #TO_NUM,
	        from_ = '+18622563399',#FROM_NUM,
            body = MSG
	    )
	    print message
        except TwilioRestException as e:
            print e
