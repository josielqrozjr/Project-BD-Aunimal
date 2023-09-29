from models import Base
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER


class Servico(Base):
    __tablename__ = "servico"
    
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)