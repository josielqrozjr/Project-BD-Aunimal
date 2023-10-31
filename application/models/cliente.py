from models import Base, Pessoa 
from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import connection
from models.pessoa import listar_pessoa, buscar_pessoa, editar_pessoa


class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())


    def __init__(self, id_cliente, data_criacao):
        self.id_cliente = id_cliente
        self.data_criacao = data_criacao


def tempo_cliente(data_criacao):
    data_atual = datetime.now()
    periodo_cliente = data_atual - data_criacao

    dias = periodo_cliente.days % 30
    meses = (periodo_cliente.days % 365) // 30  # Calcula o número de meses como parte inteira dos dias restantes divididos por 30
    anos = periodo_cliente.days // 365  # Calcula o número de anos como parte inteira dos dias divididos por 365

    return dias, meses, anos


def listar_clientes(session):
    # Consultar clientes com suas informações pessoais
    clientes = session.query(Cliente).all()
    
    for cliente in clientes:

        # Chamar a função de listar pessoa conforme o id
        listar_pessoa(session, cliente.id_cliente)

        dias, meses, anos = tempo_cliente(cliente.data_criacao)
        print(f"Cadastrado em: {cliente.data_criacao}")
        print(f"Cliente há {dias} dias, {meses} meses e {anos} anos.")
        print(f"ID Cliente: {cliente.id_cliente}\n")
        print(50 * "=")
     

def adicionar_cliente(session):

    pessoa = buscar_pessoa(session)
    
    # Criar uma nova instância de Cliente
    novo_cliente = Cliente(id_cliente = pessoa.id_pessoa,
                                   data_criacao = datetime.now())

    try:
        # Adicionar o cliente à sessão e fazer o commit
        session.add(novo_cliente)
        session.commit()
        print(50 * "-")
        print(f"Cliente cadastrado com sucesso! ID Cliente: {novo_cliente.id_cliente}")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao cadastrar o cliente: {e}")
        print(50 * "-")


def editar_cliente(session):
    cliente_id = input("Digite o ID do cliente que deseja editar: ")

    try:
        # Buscar o cliente pelo ID
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        # Exibir as informações atuais da pessoa
        dadosPessoais = cliente.pessoa
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
        print("Cliente atualizado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao editar o cliente: {e}")


def executar():
    # Iniciar uma sessão
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar clientes")
        print("2. Adicionar cliente")
        print("3. Editar cliente")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_clientes(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_cliente(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_cliente(session)
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