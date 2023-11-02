from models import Base, Funcionario
from sqlalchemy import DATETIME, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    data_pag: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    mes_ref: Mapped[date] = mapped_column(DATE, nullable=False, primary_key=True)
    id: Mapped[int] = mapped_column("id", INTEGER, ForeignKey(Funcionario.id), primary_key=True, nullable=False)

    def __init__(self, valor, data_pag, mes_ref, id):
        self.valor = valor
        self.data_pag = data_pag
        self.mes_ref = mes_ref
        self.id = id
