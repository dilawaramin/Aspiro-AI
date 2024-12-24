# Path: app/communications/sms/sms_utils.py

import re

def format_phone_number(phone_number: str) -> str:
    """Standardize phone number format for SMS sending."""
    return re.sub(r'\D', '', phone_number)  # Remove non-numeric chars

def log_sms_error(phone_number: str, error_message: str):
    """Log SMS errors for troubleshooting."""
    with open("sms_errors.log", "a") as log_file:
        log_file.write(f"Failed to send SMS to {phone_number}: {error_message}\n")
