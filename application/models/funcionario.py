from models import Base, Pessoa 
from sqlalchemy import DECIMAL, ForeignKey, DATETIME, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import connection


class Funcionario(Base):
    __tablename__ = "funcionario"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_admissao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    profissao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)

    # Relacionamento para acessar os dados de pessoa
    pessoa = relationship('Pessoa', backref='funcionario')

    def __init__(self, id_pessoa, data_admissao, profissao, salario):
       self.id_pessoa = id_pessoa
       self.data_admissao = data_admissao
       self.profissao = profissao
       self.salario = salario
 

def listar_funcionarios(session):
    # Consultar funcionários com informações de profissões e pessoas
    funcionarios = session.query(Funcionario, Pessoa).join(Pessoa).all()
    
    for funcionario, pessoa in funcionarios:
        print(50 * "-")
        print(f"ID Funcionário: {funcionario.id_funcionario}"
              f"Nome: {pessoa.nome}"
              f"Data de nascimento: {pessoa.nascimento}"
              f"CPF: {pessoa.cpf}"
              f"RG: {pessoa.rg}"
              f"Sexo: {pessoa.sexo}"
              f"Estado Civil: {pessoa.estado_civil}"
              f"Nacionalidade: {pessoa.nacionalidade}"
              f"Email: {pessoa.email}"
              f"Profissão: {funcionario.profissao}"
              f"Data Admissão: {funcionario.data_admissao}"
              f"Salário: {funcionario.salario}")

def adicionar_funcionario(session):
    # Coletar informações do funcionário
    salario = float(input("Digite o salário: "))
    estado_civil = input("Digite o estado civil: ")

    # Perguntar se o funcionário já é um associado
    is_associado = input("O funcionário já é um associado? (S/N): ").strip().lower()

    if is_associado == "s":
        # Coletar informações do associado existente
        listar_associados(session)
        associado_id = input("Digite o ID do associado existente: ")
    else:
        # Coletar informações do novo associado
        nome = input("Digite o nome do associado: ")
        nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")

        # Verificar o CPF
        while True:
            cpf = input("Digite o CPF (11 dígitos): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")

        rg = input("Digite o RG: ")
        sexo = input("Digite o sexo (M/F/NI): ")
        email = input("Digite o email: ")
        nacionalidade = input("Digite a nacionalidade: ")
        
        # Criar uma nova instância de Associado
        novo_associado = Associado(nome=nome, nascimento=nascimento, cpf=cpf, rg=rg, sexo=sexo, email=email,
                                   nacionalidade=nacionalidade, data_criacao=datetime.now())
        
        try:
            # Adicionar o novo associado à sessão e fazer o commit para obter o ID gerado
            session.add(novo_associado)
            session.commit()
            
            # Obter o ID_associado recém-gerado
            associado_id = novo_associado.id_associado
            print(f"Associado adicionado com sucesso. ID Associado: {associado_id}")
        except Exception as e:
            # Em caso de erro, faça o rollback e mostre a mensagem de erro
            session.rollback()
            print(f"Erro ao adicionar o associado: {e}")

    # Coletar informações da profissão disponível
    listar_profissoes(session)
    profissao_id = input("Digite o ID da profissão desejada: ")

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id_profissao=profissao_id, data_admissao=datetime.now(), salario=salario, estado_civil=estado_civil,
                                   id_associado=associado_id)

    try:
        # Adicionar o funcionário à sessão e fazer o commit
        session.add(novo_funcionario)
        session.commit()
        print("Funcionário adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o funcionário: {e}")


    # Coletar informações da profissão disponível
    listar_profissoes(session)
    profissao_id = input("Digite o ID da profissão desejada: ")

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id_profissao=profissao_id, data_admissao=datetime.now(), salario=salario, estado_civil=estado_civil,
                                   id_associado=associado_id)

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
            print(f"ID Funcionário: {funcionario.id_funcionario}, Nome: {funcionario.associado.nome}")

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


def listar_associados(session):
    # Consultar todos os associados disponíveis
    associados = session.query(Associado).all()

    for associado in associados:
        print(f"ID Associado: {associado.id_associado}, "
              f"Nome: {associado.nome}, "
              f"Nascimento: {associado.nascimento}, "
              f"CPF: {associado.cpf}, "
              f"RG: {associado.rg}, "
              f"Sexo: {associado.sexo}, "
              f"Email: {associado.email}")

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
        print("3. Remover funcionário")
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
            remover_funcionario(session)
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