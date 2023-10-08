from models import Base 
from sqlalchemy import DATETIME, DATE, VARCHAR, CHAR, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from typing import Literal
import sqlalchemy


Sexo = Literal['M','F','NI']
Est_civil = Literal['SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO']

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    sexo: Mapped[Sexo] = mapped_column(sqlalchemy.Enum('M','F','NI', name="sexo_enum"), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    est_civil: Mapped[Est_civil] = mapped_column(sqlalchemy.Enum('SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO', name = "est_civil_enum"), nullable=False)
    nacionalidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, default='BRASIL')
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
