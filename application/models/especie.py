from models import Base, Raca
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from typing import Literal
import sqlalchemy

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

        print(50 * "=")
        print("ESPÉCIES CADASTRADAS")
        print(50 * "=")

        for registro in especies:
            if verificar_tipo == 'TODOS' or registro.tipo == verificar_tipo:
                print(f"ID Espécie: {registro.id}  | ID Raça: {registro.id_raca}  | Tipo: {registro.tipo}")
            
        print(50 * "-")


def adicionar_especie(session):

    # Chamar função para escolher/cadastrar raça
    from models.raca import adicionar_raca
    raca_pet = adicionar_raca(session)

    listar_especies(session)
    
    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    especie_pet = solicitar_resposta("A espécie do seu pet encontra-se na lista acima? [S | N]: ")
    
    if especie_pet == 'S':
        especie_id = int(input("\nDigite o ID da espécie: "))
        especie = session.query(Especie).filter(Especie.id == especie_id).first()
        return especie
    
    else:
        # Coletar dados do novo cadastro em espécie
        tipo = input("\nDigite a espécie (GATO | CACHORRO): ")

        nova_especie = Especie(tipo = tipo, id_raca = raca_pet.id)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'espécie', nova_especie)