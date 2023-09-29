from models import Base, Raca
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Especie(Base):
    __tablename__ = "especie"

    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Enum('GATO','CACHORRO')] = mapped_column(Enum('GATO','CACHORRO'), nullable=False)
    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, ForeignKey(Raca.id_raca), autoincrement=True, nullable=False)