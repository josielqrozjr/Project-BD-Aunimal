from models import Base
from sqlalchemy import DATETIME, DATE,VARCHAR, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT
from datetime import datetime, date

class Pessoa(Base):
    __tablename__ = "pessoa"
    id: Mapped[int] = mapped_column("id", INT, 
                                            nullable=True,
                                            autoincrement=True,
                                            primary_key=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=True,
                                                    default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(200),nullable=True)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=True, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=True, unique=True)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=True)