from models import Base, Pet, Servico
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER


class Pet_servico(Base):
    __tablename__ = "pet_servico"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER, ForeignKey(Pet.id), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id), primary_key=True, nullable=False)

    def __init__(self, id_pet, id_servico):
        self.id_pet = id_pet
        self.id_servico = id_servico


def add_pet_servico(session):

    # Chamar funções para buscar/cadastrar pet e serviço
    from models.pet import buscar_pet
    pet = buscar_pet(session)

    from models.servico import adicionar_servico
    servico = adicionar_servico(session)

    novo_pet_servico = Pet_servico(id_pet = pet.id,
                                   id_servico = servico.id)
    
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(novo_pet_servico)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! \nID Pet: {novo_pet_servico.id_pet} ID Serviço: {novo_pet_servico.id_servico}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar pet-serviço: {e}")
        print(50 * "-")