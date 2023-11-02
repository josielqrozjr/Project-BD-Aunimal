from models import Base, Funcionario, Servico
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Funcionario_servico(Base):
    __tablename__ = "funcionario_servico"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id), primary_key=True, nullable=False)


    def __init__(self, id_funcionario, id_servico):
        self.id_funcionario = id_funcionario
        self.id_servico = id_servico


def add_func_servico(session):

    # Chamar funções para buscar/cadastrar funcionário e serviço
    from models.funcionario import buscar_funcionario
    funcionario = buscar_funcionario(session)

    from models.servico import adicionar_servico
    servico = adicionar_servico(session)

    novo_func_servico = Funcionario_servico(id_funcionario = funcionario.id,
                                   id_servico = servico.id)
    
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(novo_func_servico)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! \nID Funcionário: {novo_func_servico.id_pet} ID Serviço: {novo_func_servico.id_servico}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar funcionário-serviço: {e}")
        print(50 * "-")