from models import Base, Cobranca, Forma
from sqlalchemy import DECIMAL, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Cobranca_forma(Base):
    __tablename__ = "cobranca_forma"

    id: Mapped[int] = mapped_column("id", INTEGER, nullable=False, autoincrement=True, primary_key=True)
    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    parcela: Mapped[str] = mapped_column(VARCHAR(45), nullable=True)
    id_cobranca: Mapped[int] = mapped_column("id_cobranca", INTEGER,ForeignKey(Cobranca.id_cobranca), nullable=False)
    id_forma: Mapped[int] = mapped_column("id_forma", INTEGER,ForeignKey(Forma.id_forma), nullable=False)