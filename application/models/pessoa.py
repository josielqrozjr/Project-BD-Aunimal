from models import Base
from sqlalchemy import DATETIME, DATE,VARCHAR, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT
from datetime import datetime, date

class Pessoa(Base):
    __tablename__ = "pessoa"
    id: Mapped[int] = mapped_column("id", INT, 
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)