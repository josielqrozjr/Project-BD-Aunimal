from models import Base, Reserva, Pet
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Pet_reserva (Base):
    __tablename__ = "pet_reserva"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER, ForeignKey(Pet.id), primary_key=True, nullable=False) 
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id), primary_key=True, nullable=False)

    def __init__(self, id_pet, id_reserva):
        self.id_pet = id_pet
        self.id_reserva = id_reserva


def add_pet_reserva(session):

    # Chamar funções para buscar/cadastrar pet e reserva
    from models.pet import buscar_pet
    pet = buscar_pet(session)

    from models.reserva import buscar_reserva
    reserva = buscar_reserva(session)

    novo_pet_reserva = Pet_reserva(id_pet=pet.id,
                                   id_reserva=reserva.id)
    
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(novo_pet_reserva)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! \nID Reserva: {novo_pet_reserva.id_reserva} ID Pet: {novo_pet_reserva.id_pet}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar pet-reserva: {e}")
        print(50 * "-")