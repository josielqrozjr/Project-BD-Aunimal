from typing import Any
from models import Base
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER


class Raca(Base):
    __tablename__ = "raca"

    id: Mapped[int] = mapped_column("id", INTEGER, nullable=False, primary_key=True, autoincrement=True)
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
            print(f"ID Raça: {registro.id} | Classificação: {registro.classificacao}")
        
        print(50 * "-")


def adicionar_raca(session):

    listar_racas(session)

    raca_pet = input("A raça do seu pet encontra-se na lista acima? (S | N): ").strip().upper()

    while raca_pet != 'S' and raca_pet != 'N':
        print("Comando inválido! Digite novamente.")
        raca_pet
    
    if raca_pet == 'S':
        raca_id = int(input("Digite o ID da raça: "))
        raca = session.query(Raca).filter(Raca.id == raca_id).first()
        
        return raca
    
    else:
        # Coletar dados do novo cadastro em raça
        classificacao = input("Digite a classificação: ")

        nova_raca = Raca(classificacao = classificacao)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'raça', nova_raca)