from django.shortcuts import render
from twilio import twiml
from django_twilio.decorators import twilio_view
# include decompose in your views.py
from django_twilio.requests import decompose
from hetaira.parser import MessageParser, TokenizerError, ParsingError

@twilio_view
def message(request):
     response = twiml.response()

    # Create a new TwilioRequest object
    twilio_request = decompose(request)

    # See the Twilio attributes on the class
    message_from = twilio_request["from"]
    if twilio_request.type is 'message':
        #we parse this


        #send message back
        response.message(msg, to)
    else
        response.leave()

    return response
