import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models import User, Message
from datetime import datetime

logger = logging.getLogger(__name__)


def add_message(db: Session, user_number: str, message_content: str, sender: str):
    """
    Add a message to the database for a specific user.

    :param db: SQLAlchemy session
    :param user_number: The phone number of the user
    :param message_content: The content of the message
    :param sender: The sender of the message ("user" or "system")
    :return: The newly created Message object
    """

    try:
        
        # Validate inputs
        if not user_number or not isinstance(user_number, str):
            raise ValueError("Invalid user number provided")
        if not message_content or not isinstance(message_content, str):
            raise ValueError("Invalid message content provided")
        if sender not in {"user", "system"}:
            raise ValueError("Sender must be 'user' or 'system'")
        
        # Fetch the user
        user = db.query(User).filter(User.number == user_number).first()
        
        # NOTE: Change ths later to add user with subscription status of false
        if not user:
            raise ValueError(f"User with number {user_number} not found")
        
        # Create a new message object
        new_message = Message(
            user_number=user_number,
            date=datetime.now(),
            message=message_content,
            sender=sender
        )
        
        # commit the new message to DB
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        
        return new_message
    
    # raise and log errors
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database operation failed: {str(e)}")
        raise RuntimeError(f"Database operation failed: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        db.rollback()
        raise

def add_user(db: Session, name: str, email: str, phone_number: str):
    """
    Create a new user in the database.

    :param db: SQLAlchemy session
    :param name: The name of the user
    :param email: The email of the user
    :param phone_number: The phone number of the user (primary key)
    :return: The newly created User object
    """
    
    try:
        # Validate inputs
        if not name or not isinstance(name, str):
            raise ValueError("Invalid name provided")
        if not email or not isinstance(email, str):
            raise ValueError("Invalid email provided")
        if not phone_number or not isinstance(phone_number, str):
            raise ValueError("Invalid phone number provided")
        
        # Create a new user object
        new_user = User(
            number=phone_number,
            name=name,
            subscribed=False  # Default subscription status is False
        )
        
        # Commit the new user to the database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
        
    # Handle database-related errors
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database operation failed: {str(e)}")
        raise RuntimeError(f"Database operation failed: {str(e)}")
    
    # Handle unexpected errors
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        db.rollback()
        raise
    
