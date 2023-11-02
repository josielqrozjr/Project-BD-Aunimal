from models import Base, Reserva, Servico
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Reserva_servico(Base):
    __tablename__ = "reserva_servico"

    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id), primary_key=True, nullable=False) 


    def __init__(self, id_reserva, id_servico):
        self.id_reserva = id_reserva
        self.id_servico = id_servico


def add_reserva_serv(session):

    # Chamar funções para buscar/cadastrar reserva e serviço
    from models.reserva import buscar_reserva
    reserva = buscar_reserva(session)

    from models.servico import adicionar_servico
    servico = adicionar_servico(session)

    nova_reserva_serv = Reserva_servico(id_reserva = reserva.id,
                                   id_servico = servico.id)
    
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(nova_reserva_serv)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! \nID Reserva: {nova_reserva_serv.id_reserva} ID Serviço: {nova_reserva_serv.id_servico}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar reserva-serviço: {e}")
        print(50 * "-")