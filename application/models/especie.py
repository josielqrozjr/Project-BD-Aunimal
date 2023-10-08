from models import Base, Raca
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from typing import Literal
import sqlalchemy

Tipo = Literal['GATO','CACHORRO']

class Especie(Base):
    __tablename__ = "especie"

    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Tipo] = mapped_column(sqlalchemy.Enum('GATO','CACHORRO', name="tipo_enum"), nullable=False)
    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, ForeignKey(Raca.id_raca), autoincrement=True, nullable=False)