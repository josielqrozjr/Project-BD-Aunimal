from models import Base, Especie, Cliente 
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, DATE, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from services.db import connection
from typing import Literal
import sqlalchemy
from models.cliente import buscar_cliente

Sexo = Literal['M','F']
Porte = Literal['PP', 'P', 'M', 'G', 'GG']

class Pet(Base):
    __tablename__ = "pet"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(5,2), nullable=True)
    sexo: Mapped[Sexo] = mapped_column(sqlalchemy.Enum('M','F', name="sexo_enum"), nullable=False)
    pelagem: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    porte: Mapped[Porte] = mapped_column(sqlalchemy.Enum('PP', 'P', 'M', 'G', 'GG', name = "porte_enum"), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=True)
    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER, ForeignKey(Especie.id_especie), primary_key=True, nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Cliente.id_cliente), nullable=False)


def cadastrar_pet(session):

    buscar_cliente
    
    

def executar():
    # Iniciar uma sessão
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar pets")
        print("2. Adicionar pet")
        print("3. Editar pet")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_pets(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_pet(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_pet(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()