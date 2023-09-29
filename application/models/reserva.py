from models import Base, Cliente, Funcionario
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime

class Reserva(Base):
    __tablename__ = "reserva"
    
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    check_in: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    checkout: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    descricao: Mapped[str] = mapped_column(VARCHAR(200),nullable=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2),nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente",INTEGER, ForeignKey(Cliente.id_cliente), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), nullable=False)