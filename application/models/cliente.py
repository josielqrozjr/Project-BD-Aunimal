from models import Base, Pessoa 
from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import connection
from models.pessoa import listar_pessoa, buscar_pessoa, editar_pessoa


class Cliente(Base):
    __tablename__ = "cliente"
    
    id: Mapped[int] = mapped_column("id", INTEGER, ForeignKey(Pessoa.id), primary_key=True, nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())

    def __init__(self, data_criacao):
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
        listar_pessoa(session, cliente.id)

        dias, meses, anos = tempo_cliente(cliente.data_criacao)
        print(f"Cadastrado em: {cliente.data_criacao}")
        print(f"Cliente há {dias} dias, {meses} meses e {anos} anos.")
        print(f"ID Cliente: {cliente.id}\n")
        print(50 * "=")
     

def adicionar_cliente(session):

    pessoa = buscar_pessoa(session)
    
    # Criar uma nova instância de Cliente
    novo_cliente = Cliente(id = pessoa.id,
                                   data_criacao = datetime.now())

    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'cliente', novo_cliente)    


def editar_cliente(session):

    #Chamar a função para identificar a pessoa correspondente
    pessoa = editar_pessoa(session)

    try:
        # Buscar o funcionário pelo ID
        cliente = session.query(Cliente).filter(Cliente.id == pessoa.id).one()

        # Exibir as informações atuais do funcionário
        print(50 * '=')
        print('CLIENTE ENCONTRADO')
        print(50 * '-')
        print(f"ID Cliente: {cliente.id}")
        print(f"Cadastrado em: {cliente.data_criacao}")

        session.commit()
        print(50 * "-")
        print("Cliente atualizado com sucesso!")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao atualizar o cliente: {e}")
        print(50 * "-")


# Função para buscar pessoa associada a tabela cliente
def buscar_cliente(session):

    # Perguntar se possui cadastro
    verificar_cadastro = input("\nPossui cadastro como cliente no sistema? [S | N]: ").strip().lower()

    if verificar_cadastro == "s":

        # Consultar cliente por CPF
        cpf_pessoa = input("Digite o CPF para consultar: ")
        cliente_query = session.query(Pessoa).join(Cliente, Pessoa.id == Cliente.id).filter(Pessoa.cpf == cpf_pessoa).first()

        # Verifique se a pessoa foi encontrada
        if cliente_query:
                print(50 * "=")
                print('CLIENTE ENCONTRADO')
                print(50 * '-')
                print(f"ID Cliente: {cliente_query.id}")
                print(f"Nome: {cliente_query.nome}")
                print(50 * '-')

                return cliente_query
        
        else:
            print(50 * '-')
            print("Cadastro de cliente não encontrado!")
            question_cadastro = input("Deseja realizar o cadastro? [S | N]:").strip().lower()

            if question_cadastro == "s": return adicionar_cliente(session)
            else: 
                from models.tabelas import executar
                executar()
        
    else: return adicionar_cliente(session)


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