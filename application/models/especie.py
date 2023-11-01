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

    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Tipo] = mapped_column(sqlalchemy.Enum('GATO','CACHORRO', name="tipo_enum"), nullable=False)
    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, ForeignKey(Raca.id_raca), autoincrement=True, nullable=False)

    def __init__(self, tipo, id_raca):
        self.tipo = tipo
        self.id_raca = id_raca


def listar_especies(session):

    especies = session.query(Especie).all()

    print(50 * "=")
    print("ESPÉCIES CADASTRADAS")
    print(50 * "=")

    verificar_tipo = input("Escolha o tipo para listar (GATO | CACHORRO | TODOS): ").strip().upper()

    for registro in especies:

        if verificar_tipo == 'TODOS' or registro.tipo == verificar_tipo:
            print(f"\nID Espécie: {registro.id_especie}  | ID Raça: {registro.id_raca}  | Tipo: {registro.tipo}")
        
    print(50 * "-")


def adicionar_especie(session):

    listar_especies(session)
    