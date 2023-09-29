from services.db import session
from models import *
from utils.database_utils import create_db

if __name__ == "__main__":
    print("Criando o Banco de Dados!")
    create_db()

