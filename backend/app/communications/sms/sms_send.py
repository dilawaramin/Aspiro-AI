# Path: app/communications/sms/sms_send.py
import os
from dotenv import load_dotenv

load_dotenv() 
# need the api for this
from twilio.rest import Client

from sms_utils import format_phone_number, log_sms_error

# Load environment variables (e.g., API keys)
load_dotenv() 
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")


class SMSService:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, to: str, message: str):
        try:
            to = format_phone_number(to)  # Utility to clean up phone numbers
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=to
            )
            return message.sid
        except Exception as e:
            log_sms_error(to, str(e))
            raise RuntimeError(f"Failed to send SMS to {to}. Error: {e}")
