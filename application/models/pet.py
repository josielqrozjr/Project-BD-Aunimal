from models import Base, Especie, Cliente 
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, DATE, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from typing import Literal
import sqlalchemy

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
    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER, ForeignKey(Especie.id_especie), primary_key=True, nullable=False) # chave PK Fk coloca junto?
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Cliente.id_cliente), nullable=False)