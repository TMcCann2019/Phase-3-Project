from config import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

if __name__ == "__main__":
  with app.app_context():
    pass
    # remove pass and write your seed data
