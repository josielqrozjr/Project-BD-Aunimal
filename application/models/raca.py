from typing import Any
from models import Base
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from services.db import connection


class Raca(Base):
    __tablename__ = "raca"

    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, nullable=False, primary_key=True, autoincrement=True)
    classificacao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)

    def __init__(self, classificacao):
        self.classificacao = classificacao


def listar_racas(session):

    racas = session.query(Raca).all()

    if not racas:
        print(50 * "=")
        print("NÃO EXISTEM RAÇAS CADASTRADAS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("RAÇAS CADASTRADAS")
        print(50 * "=")

        for registro in racas:
            print(f"\nID Raça: {registro.id_raca} | Classificação: {registro.classificacao}")
        
        print(50 * "-")


def adicionar_raca(session):

    listar_racas(session)

    raca_pet = input("A raça do seu pet encontra-se na lista acima? (S | N): ").strip().upper()

    while raca_pet != 'S' and raca_pet != 'N':
        print("Comando inválido! Digite novamente.")
        raca_pet = input("A raça do seu pet encontra-se na lista acima? (S | N): ").strip().upper()
    
    if raca_pet == 'S':
        raca_id = int(input("Digite o ID da raça: "))
        return raca_id
    
    else:
        # Coletar dados do novo cadastro em raça
        classificacao = input("Digite a classificação: ")

        nova_raca = Raca(classificacao = classificacao)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'raca', nova_raca)


def executar():
    # Iniciar uma sessão
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar raças")
        print("2. Adicionar raça")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_racas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_raca(session)
        elif escolha == "3":
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


    
    