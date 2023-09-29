from services.db import engine
from models import *

def create_db():
    Base.metadata.create_all(bind=engine)