from sqlalchemy.orm import Session
from models import User, Message
from datetime import datetime


def add_message(db: Session, user_number: str, message_content: str, sender: str):
    """
    Add a message to the database for a specific user.

    :param db: SQLAlchemy session
    :param user_number: The phone number of the user
    :param message_content: The content of the message
    :param sender: The sender of the message ("user" or "system")
    :return: The newly created Message object
    """
    # Fetch the user
    user = db.query(User).filter(User.number == user_number).first()
    
    # NOTE: Change ths later to add user with subscription status of false
    if not user:
        raise ValueError(f"User with number {user_number} not found")
    
    new_message = Message(
        user_number=user_number,
        date=datetime.now(),
        message=message_content,
        sender=sender
    )
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)