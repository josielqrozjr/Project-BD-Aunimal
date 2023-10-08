from models import Base, Pessoa 
from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime


class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False, autoincrement=True, primary_key=True)
    id_pessoa = Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    id_pessoa = Column(Integer, ForeignKey('associado.id_pessoa'), nullable=False)
    
    # Adicione um relacionamento para acessar os dados do associado
    pessoa = relationship('pessoa', backref='cliente')

    def __init__(self, id_pessoa):
        self.id_pessoa = id_pessoa
  