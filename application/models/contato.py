from models import Base, Pessoa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, TINYINT


class Contato(Base):
    __tablename__ = "contato"

    codigo_pais: Mapped[int] = mapped_column(TINYINT(3, unsigned=True, zerofill=True), nullable=False)
    codigo_area: Mapped[int] = mapped_column(TINYINT(unsigned=True), nullable=False)
    numero: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)