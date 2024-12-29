import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, Blueprint
from twilio.twiml.messaging_response import MessagingResponse

# setup flask app (?)
sms_blueprint = Blueprint('sms', __name__)


@sms_blueprint.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)

    # Start our TwiML response
    resp = MessagingResponse()

    # returns empty TwiML response
    return str(resp)
