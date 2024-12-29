import os
from dotenv import load_dotenv
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# setup flask app (?)
app = Flask(__name__)
load_dotenv()
ROOT_HOST = os.getenv("ROOT_DOMAIN")

@app.route("/communications/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)

    # Start our TwiML response
    resp = MessagingResponse()

    # returns empty TwiML response
    return str(resp)

# testing
if __name__ == "__main__":
    app.run(port=3000, debug=True)
    
    