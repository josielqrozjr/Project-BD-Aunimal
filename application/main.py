from services.database import session
from models import *
from utils.database_utils import create_db
# python3 -m pip install pymysql sqlalchemy sqlalchemy-utils

if __name__ == "__main__":
    print("Criando o Banco de Dados!")
    create_db()
    
    # Mostrar a tabela selecionada, tipo o SELECT no SQL
    #pessoa_list: list[Pessoa] = session.query(Pessoa).all()