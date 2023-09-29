from models import Base, Funcionario
from sqlalchemy import DATETIME, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    data_pagamento: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    mes_referencia: Mapped[date] = mapped_column(DATE, nullable=False, primary_key=True)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), primary_key=True, nullable=False)  