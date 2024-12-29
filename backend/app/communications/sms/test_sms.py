from sms_utils import format_phone_number
from backend.app.communications.sms.sms_send import SMSService


# phone_number = input("Enter the Phone number to test with: ")
# something = format_phone_number(phone_number)

# print("The returned phone number from format_phone_number method is: ", something)



# Define the recipient's phone number and the message
recipient_phone_unformated = input("Enter the phone number to send the test message to:") # Replace with the recipient's phone number
recipient_phone = format_phone_number(recipient_phone_unformated)
message_content = "Hello! This is a test message from SMSService."


# Send the message
sms_service = SMSService()
try:
    message_sid = sms_service.send_sms(recipient_phone, message_content)
    print(f"Message sent successfully! SID: {message_sid}")
except RuntimeError as e:
    print(f"Failed to send message. Error: {e}")



