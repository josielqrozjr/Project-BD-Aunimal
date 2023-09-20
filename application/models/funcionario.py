from models import Base, Pessoa
from sqlalchemy import DATETIME, DATE,VARCHAR, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date

class Funcionario(Base):
    __tablename__ = "funcionario"
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Pessoa.id_pessoa), 
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