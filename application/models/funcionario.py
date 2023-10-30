from models import Base, Pessoa
from sqlalchemy import DECIMAL, ForeignKey, DATETIME, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import connection
from models.endereco import cadastrar_endereco
from models.pessoa import listar_pessoa, buscar_pessoa

class Funcionario(Base):
    __tablename__ = "funcionario"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_admissao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    profissao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)


    def __init__(self, id_pessoa, data_admissao, profissao, salario):
       self.id_pessoa = id_pessoa
       self.data_admissao = data_admissao
       self.profissao = profissao
       self.salario = salario
 

def listar_funcionarios(session):
    # Consultar funcionários com informações de profissões e pessoas
    funcionarios = session.query(Funcionario).all()
    
    for funcionario in funcionarios:
        print(50 * "=")
        print(f"ID Funcionário: {funcionario.id_funcionario}"
              f"Profissão: {funcionario.profissao}"
              f"Data Admissão: {funcionario.data_admissao}"
              f"Salário: {funcionario.salario}")
        
        # Chamar a função de listar pessoa conforme o id
        listar_pessoa(session, funcionario.id_funcionario)


def adicionar_funcionario(session):

    pessoa_id = buscar_pessoa(session)

    # Coletar informações do funcionário
    profissao = input("Digite a profissão: ")
    salario = float(input("Digite o salário: "))

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id_pessoa = pessoa_id,
                                   data_admissao = datetime.now(),
                                   profissao = profissao, 
                                   salario = salario)

    try:
        # Adicionar o funcionário à sessão e fazer o commit
        session.add(novo_funcionario)
        session.commit()
        print("Funcionário adicionado com sucesso!")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o funcionário: {e}")


def remover_funcionario(session):
    try:
        # Consultar funcionários
        funcionarios = session.query(Funcionario).all()
        
        if not funcionarios:
            print("Não há funcionários para excluir.")
            return

        print("Funcionários disponíveis para exclusão:")
        for funcionario in funcionarios:
            print(f"ID Funcionário: {funcionario.id_funcionario}, Nome: {funcionario.pessoa.nome}")

        funcionario_id = input("Digite o ID do funcionário que deseja excluir ou '0' para cancelar: ")

        if funcionario_id == '0':
            print("Operação de exclusão cancelada.")
        else:
            try:
                # Buscar o funcionário pelo ID
                funcionario = session.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).one()

                # Remover o funcionário
                session.delete(funcionario)
                session.commit()
                print("Funcionário excluído com sucesso!")
            except Exception as e:
                # Em caso de erro, faça o rollback e mostre a mensagem de erro
                session.rollback()
                print(f"Erro ao excluir o funcionário: {e}")
    except Exception as e:
        print(f"Erro ao listar funcionários: {e}")


def listar_funcionarios(session):
    # Consultar todos os funcionários disponíveis
    dados_funcionarios = session.query(Funcionario, Pessoa).join(Pessoa).all()

    for funcionario, dadosPessoais in dados_funcionarios:
        print(50 * "-")
        print(f"ID Cliente: {funcionario.id_funcionario} \nNome: {dadosPessoais.nome} \nCPF: {dadosPessoais.cpf} \nRG: {dadosPessoais.rg} \nNascimento: {dadosPessoais.nascimento} \nSexo: {dadosPessoais.sexo} \nEmail: {dadosPessoais.email} \nEstado Civil: {dadosPessoais.est_civil} \nNacionalidade: {dadosPessoais.nacionalidade} \nProfissão: {funcionario.profissao} \nSalário: {funcionario.salario} \nAdmitido em: {funcionario.data_admissao}")


def editar_funcionario(session):
    
    funcionario_id = input("Digite o ID do funcionário que deseja editar: ")

    try:
        # Buscar o funcionário pelo ID
        funcionario = session.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).one()

        # Exibir as informações atuais da pessoa
        dadosPessoais = funcionario.pessoa
        print(f"Informações atuais da pessoa:")
        print(f"Nome: {dadosPessoais.nome}")
        print(f"Nascimento: {dadosPessoais.nascimento}")
        print(f"CPF: {dadosPessoais.cpf}")
        print(f"RG: {dadosPessoais.rg}")
        print(f"Sexo: {dadosPessoais.sexo}")
        print(f"Email: {dadosPessoais.email}")
        print(f"Estado Civil: {dadosPessoais.est_civil}")
        print(f"Nacionalidade: {dadosPessoais.nacionalidade}")

        # Coletar as novas informações da pessoa
        nome = input("Digite o novo nome da pessoa: ")
        nascimento = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
        cpf = input("Digite o novo CPF: ")
        rg = input("Digite o novo RG: ")
        sexo = input("Digite o novo sexo (M/F/NI): ")
        email = input("Digite o novo email: ")
        est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
        nacionalidade = input("Digite a nova nacionalidade: ")

        # Atualizar as informações da pessoa
        dadosPessoais.nome = nome
        dadosPessoais.nascimento = nascimento
        dadosPessoais.cpf = cpf
        dadosPessoais.rg = rg
        dadosPessoais.sexo = sexo
        dadosPessoais.email = email
        dadosPessoais.est_civil = est_civil
        dadosPessoais.nacionalidade = nacionalidade

        session.commit()
        print("Funcionário atualizado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao editar o funcionário: {e}")
        

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
        print("4. Remover funcionário")
        print("5. Sair")

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
            remover_funcionario(session)
        elif escolha == "5":
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