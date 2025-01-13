import os
import logging
from dotenv import load_dotenv
from flask import Flask, request, redirect, Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from database.db import SessionLocal
from database.models import User, Message
from database.db import get_db
from database.queries import create_user


# Create a blueprint for the signup route
signup_bp = Blueprint('signup', __name__)

# Initialize logger
logger = logging.getLogger(__name__)


@signup_bp.route('/user/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    # extract user data
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    
    # Validate inputs
    if not name or not isinstance(name, str):
        return jsonify({"error": "Invalid name provided"}), 400
    if not email or not isinstance(email, str):  # Add more email validation here if needed
        return jsonify({"error": "Invalid email provided"}), 400
    if not phone or not isinstance(phone, str):
        return jsonify({"error": "Invalid phone number provided"}), 400
    
    # Get the database session
    db = next(get_db())
    
    try: 
        # Create the new user
        new_user = create_user(db.session, name=name, email=email, phone_number=phone)
        return jsonify({
            "message": "User successfully signed up for the notification list",
            "user": {
                "name": new_user.name,
                "email": email,
                "phone": phone,
                "subscribed": new_user.subscribed
            }
        }), 201
    
    except Exception as e:
        # Return a generic error response for unexpected exceptions
        # NOTE:
        # Add more specific error handling here later 
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": str(e)}), 500