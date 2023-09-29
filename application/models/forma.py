from models import Base
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Forma(Base):
    __tablename__ = "forma"

    id_forma: Mapped[int] = mapped_column("id_forma", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
