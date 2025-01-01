import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, Blueprint
from twilio.twiml.messaging_response import MessagingResponse

from sms_utils import format_phone_number
from database.db import SessionLocal
from database.models import User, Message
from database.db import get_db
from database.queries import add_message
from datetime import datetime


# setup flask blueprint
sms_blueprint = Blueprint('sms', __name__)


@sms_blueprint.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    user_number = format_phone_number(request.values.get('From', None))
    date_received = datetime.now()
    
    # DEBUG
    print(body)
    
    # save the message to database
    db = next(get_db())
    
    try:
        # call add_message from queries.py
        new_message = add_message(db, user_number, body, "user")
        print(f"Message added: {new_message}")
        
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        # Ensure the session is closed
        db.close() 
        
        
    """
    Add GPT prompting + message send here
    """
    
    
    # Start our TwiML response (returning an empty response for now)
    resp = MessagingResponse()
    return str(resp)
