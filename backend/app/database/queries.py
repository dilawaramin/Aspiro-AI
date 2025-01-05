from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Database configuration
DATABASE_URL = "postgresql+psycopg2://aspiro:aspiro123@database-1.chac608iwr2f.us-east-1.rds.amazonaws.com/aspirodb"

# SQLAlchemy setup

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Define Users table
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone = Column(String(15), unique=True, nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    goals = relationship("Goal", back_populates="user")
    messages = relationship("Message", back_populates="user")

# Define Goals table
class Goal(Base):
    __tablename__ = "Goals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    goal_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="goals")

# Define Message History table
class Message(Base):
    __tablename__ = "Messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="messages")

# Create all tables (if they don't exist)
Base.metadata.create_all(engine)

# Function definitions
def get_user_messages_by_number():
    phone = input("Enter the user's phone number: ")
    user = session.query(User).filter_by(phone=phone).first()
    if user:
        print(f"\nMessage History for {user.username} ({phone}):")
        for message in user.messages:
            print(f"[{message.created_at}] {message.message_text}")
    else:
        print("User not found.")

def get_user_by_email():
    email = input("Enter the user's email: ")
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(f"\nUser Profile:\nID: {user.id}\nUsername: {user.username}\nPhone: {user.phone}\nEmail: {user.email}")
    else:
        print("User not found.")

def get_user_by_phone():
    phone = input("Enter the user's phone number: ")
    user = session.query(User).filter_by(phone=phone).first()
    if user:
        print(f"\nUser Profile:\nID: {user.id}\nUsername: {user.username}\nPhone: {user.phone}\nEmail: {user.email}")
    else:
        print("User not found.")

def get_all_users():
    users = session.query(User).all()
    if users:
        print("\nAll Users:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Phone: {user.phone}, Email: {user.email}")
    else:
        print("No users found.")

def get_user_goals_by_number():
    phone = input("Enter the user's phone number: ")
    user = session.query(User).filter_by(phone=phone).first()
    if user:
        print(f"\nGoals for {user.username} ({phone}):")
        for goal in user.goals:
            print(f"[{goal.created_at}] {goal.goal_text}")
    else:
        print("User not found.")

def add_goal_to_user():
    phone = input("Enter the user's phone number: ")
    goal_text = input("Enter the goal: ")
    user = session.query(User).filter_by(phone=phone).first()
    if user:
        new_goal = Goal(goal_text=goal_text, user=user)
        session.add(new_goal)
        session.commit()
        print("Goal added successfully!")
    else:
        print("User not found.")

def add_phone_to_user():
    email = input("Enter the user's email: ")
    phone = input("Enter the new phone number: ")
    user = session.query(User).filter_by(email=email).first()
    if user:
        user.phone = phone
        session.commit()
        print("Phone number added successfully!")
    else:
        print("User not found.")

# Main admin menu
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Retrieve a user's text history by phone number")
        print("2. Retrieve a user profile by email")
        print("3. Retrieve a user profile by phone number")
        print("4. Retrieve all users")
        print("5. Retrieve a user's goals by phone number")
        print("6. Add a goal to a user by phone number")
        print("7. Add a phone number to a user profile by email")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            get_user_messages_by_number()
        elif choice == "2":
            get_user_by_email()
        elif choice == "3":
            get_user_by_phone()
        elif choice == "4":
            get_all_users()
        elif choice == "5":
            get_user_goals_by_number()
        elif choice == "6":
            add_goal_to_user()
        elif choice == "7":
            add_phone_to_user()
        elif choice == "8":
            print("Exiting admin menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

# Run the admin menu
if __name__ == "__main__":
    try:
        print("Connected to the AWS database!")
        admin_menu()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
        print("Session closed.")
