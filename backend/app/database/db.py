# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Load environment variables
# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Create engine and session
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)

# # Declarative base for models
# Base = declarative_base()

# # Function to initialize the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

import psycopg2
from getpass import getpass

# AWS Database credentials
db_config = {
    "dbname": "aspirodb",
    "user": "aspiro",
    "password": "aspiro123",
    "host": "database-1.chac608iwr2f.us-east-1.rds.amazonaws.com",
    "port": 5432
}



# Queries for login system
create_user_query = """
INSERT INTO public."Users" (username, password, phone, email)
VALUES (%s, %s, %s, %s)
RETURNING id;
"""
login_query = 'SELECT * FROM public."Users" WHERE username = %s AND password = %s;'
fetch_all_users_query = 'SELECT id, username, email, phone, created_at FROM public."Users";'

# Function to create a new account
def create_account(cursor):
    print("\n--- Create New Account ---")
    username = input("Enter a username: ")
    password = getpass("Enter a password: ")  # Hidden input for security
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")

    try:
        cursor.execute(create_user_query, (username, password, phone, email))
        user_id = cursor.fetchone()[0]
        print(f"Account created successfully! Your user ID is {user_id}.")
    except psycopg2.Error as e:
        print(f"Error creating account: {e}")

# Function to log in
def log_in(cursor):
    print("\n--- Log In ---")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")  # Hidden input for security

    try:
        cursor.execute(login_query, (username, password))
        user = cursor.fetchone()
        if user:
            print(f"Welcome back, {user[1]}! You logged in successfully.")
        else:
            print("Invalid username or password. Please try again.")
    except psycopg2.Error as e:
        print(f"Error during login: {e}")

# Function to check all accounts
def check_all_accounts(cursor):
    print("\n--- All Registered Accounts ---")
    try:
        cursor.execute(fetch_all_users_query)
        users = cursor.fetchall()
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Phone: {user[3]}, Created At: {user[4]}")
    except psycopg2.Error as e:
        print(f"Error fetching accounts: {e}")

# Main program
def main():
    try:
        # Connect to AWS PostgreSQL database
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        print("Connected to the AWS database!")

        

        # Login system menu
        while True:
            print("\n--- Login System ---")
            print("1. Create New Account")
            print("2. Log In")
            print("3. Check All Accounts")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                create_account(cursor)
                connection.commit()  # Commit changes
            elif choice == "2":
                log_in(cursor)
            elif choice == "3":
                check_all_accounts(cursor)
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
