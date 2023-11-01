from models import Base, Raca
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from typing import Any, Literal
import sqlalchemy
from models.raca import listar_racas

Tipo = Literal['GATO','CACHORRO']

class Especie(Base):
    __tablename__ = "especie"

    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Tipo] = mapped_column(sqlalchemy.Enum('GATO','CACHORRO', name="tipo_enum"), nullable=False)
    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, ForeignKey(Raca.id), autoincrement=True, nullable=False)

    def __init__(self, tipo, id_raca):
        self.tipo = tipo
        self.id_raca = id_raca


def listar_especies(session):

    especies = session.query(Especie).all()

    if not especies:
        print(50 * "=")
        print("NÃO EXISTEM ESPÉCIES CADASTRADAS")
        print(50 * "=")    

    else:

        print(50 * "-")
        verificar_tipo = input("\nEscolha o tipo para listar (GATO | CACHORRO | TODOS): ").strip().upper()

        print("\n", 50 * "=")
        print("ESPÉCIES CADASTRADAS")
        print(50 * "=")

        for registro in especies:

            if verificar_tipo == 'TODOS' or registro.tipo == verificar_tipo:
                print(f"\nID Espécie: {registro.id}  | ID Raça: {registro.id_raca}  | Tipo: {registro.tipo}")
            
        print(50 * "-" + "\n")


def adicionar_especie(session):

    # Chamar função para escolher/cadastrar raça
    from models.raca import adicionar_raca
    raca_pet = adicionar_raca(session)

    listar_especies(session)
    
    especie_pet = input("A espécie do seu pet encontra-se na lista acima? (S | N): ").strip().upper()

    while especie_pet != 'S' and especie_pet != 'N':
        print("Comando inválido! Digite novamente.")
        especie_pet
    
    if especie_pet == 'S':
        raca_id = int(input("Digite o ID da raça: "))
        return raca_id
    
    else:
        # Coletar dados do novo cadastro em raça
        classificacao = input("Digite a classificação: ")

        nova_especie = Raca(classificacao = classificacao)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'espécie', nova_especie)
    

def executar():
    # Iniciar uma sessão
    from services.db import connection
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Adicionar espécie")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            adicionar_especie(session)
        elif escolha == "2":
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