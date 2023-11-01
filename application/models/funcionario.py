from models import Base, Pessoa
from sqlalchemy import DECIMAL, ForeignKey, DATETIME, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import connection
from models.pessoa import listar_pessoa, buscar_pessoa, editar_pessoa

class Funcionario(Base):
    __tablename__ = "funcionario"

    id: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Pessoa.id), primary_key=True, nullable=False)
    data_admissao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    profissao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)


    def __init__(self, data_admissao, profissao, salario):
       self.data_admissao = data_admissao
       self.profissao = profissao
       self.salario = salario


def listar_funcionarios(session):
    # Consultar funcionários com informações de profissões e pessoas
    funcionarios = session.query(Funcionario).all()
    
    for funcionario in funcionarios:

        # Chamar a função de listar pessoa conforme o id
        listar_pessoa(session, funcionario.id)

        print(f"Profissão: {funcionario.profissao}"
              f"\nData Admissão: {funcionario.data_admissao}"
              f"\nSalário: {funcionario.salario}"
              f"\nID Funcionário: {funcionario.id}\n")
        print(50 * "=")


def adicionar_funcionario(session):

    pessoa = buscar_pessoa(session)

    # Coletar informações do funcionário
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE FUNCIONÁRIO')
    print(50 * '=')
    profissao = input("Digite a profissão: ")
    salario = float(input("Digite o salário: "))

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id = pessoa.id,
                                   data_admissao = datetime.now(),
                                   profissao = profissao, 
                                   salario = salario)

    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'funcionário', novo_funcionario)


def editar_funcionario(session):

    #Chamar a função para identificar a pessoa correspondente
    pessoa = editar_pessoa(session)

    try:
        # Buscar o funcionário pelo ID
        funcionario = session.query(Funcionario).filter(Funcionario.id == pessoa.id).one()

        # Exibir as informações atuais do funcionário
        print(50 * '=')
        print('FUNCIONÁRIO ENCONTRADO')
        print(50 * '-')
        print(f"ID Funcionário: {funcionario.id}")
        print(f"Profissão: {funcionario.profissao}")
        print(f"Salário: {funcionario.salario}")
        print(f"Data Admissão: {funcionario.data_admissao}")
        
        # Coletar as novas informações da funcionário
        print(50 * '=')
        print('FORMULÁRIO PARA ATUALIZAR FUNCIONÁRIO')
        print(50 * '=')
        profissao = input("Digite a profissão: ")
        salario = float(input("Digite o salário: "))

        # Atualizar as informações próprias do funcionário
        funcionario.profissao = profissao
        funcionario.salario = salario

        session.commit()
        print(50 * "-")
        print("Funcionário atualizado com sucesso!")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao atualizar o funcionário: {e}")
        print(50 * "-")
        

def executar():
    # Iniciar uma sessão
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar funcionários")
        print("2. Adicionar funcionário")
        print("3. Editar funcionário")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_funcionarios(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_funcionario(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_funcionario(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()    