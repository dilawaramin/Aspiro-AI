import sqlalchemy as SQL
from .db import Base


class User(Base):
    __tablename__ = "users"
    number = SQL.Column(SQL.String, primary_key=True) # primary key: phone number
    name = SQL.Column(SQL.String)
    subscribed = SQL.Column(SQL.Boolean) # is the user subscribed to our service?
    
    # message history relationship
    messages = SQL.orm.relationship("Message", backref="user")
    
    
class Message(Base):
    __tablename__ = "messages"
    id = SQL.Column(SQL.Integer, primary_key=True, autoincrement=True)
    user_number = SQL.Column(SQL.String, SQL.ForeignKey("users.number"))
    date = SQL.Column(SQL.DateTime)
    message = SQL.Column(SQL.Text)
    sender = SQL.Column(SQL.String) # ex. "user" or "system"