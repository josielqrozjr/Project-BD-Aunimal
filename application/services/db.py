from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

password = "2n#*uB?w!r_O"
instance = f"mysql+pymysql://root:{quote(password)}@localhost:3306/Auunimal"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
connection = Session(bind=engine, autocommit=False, autoflush=True)