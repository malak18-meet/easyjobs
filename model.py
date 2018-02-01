from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash
Base = declarative_base()

class User(UserMixin, Base):
    __tablename__  = 'user'
    id             = Column(Integer, primary_key=True)
    first_name     = Column(String)
    last_name      = Column(String)
    email          = Column(String)
    pw_hash        = Column(String)
    photo          = Column(String)
    authenticated  =Column(Boolean,default=False)

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)



class Job(Base):
    __tablename__  = 'Job'
    id             = Column(Integer, primary_key=True)
    job            = Column(String)
    about          = Column(String)
    frequency      = Column(String)
    date           = Column(String)
    payment        = Column(Integer)
    picture        = Column(String)
    email          = Column(String)
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel