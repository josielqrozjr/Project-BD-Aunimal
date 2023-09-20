from models import Base
from sqlalchemy import DATETIME, DATE,VARCHAR, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date

class Pessoa(Base):
    __tablename__ = "pessoa"
    id: Mapped[int] = mapped_column("id", INTEGER, 
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=False,
                                                    default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(200),nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)