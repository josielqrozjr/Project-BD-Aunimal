from models import Base, Cliente, Funcionario, Pessoa
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime

class Reserva(Base):
    __tablename__ = "reserva"
    
    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    check_in: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    checkout: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    descricao: Mapped[str] = mapped_column(VARCHAR(200),nullable=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2),nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente",INTEGER, ForeignKey(Cliente.id), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id), nullable=False)

    def __init__(self, check_in, checkout, descricao, 
                 valor_total, id_cliente, id_funcionario):
        self.check_in = check_in
        self.checkout = checkout
        self.descricao = descricao
        self.valor_total = valor_total
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario


# Função para adicionar dados em reserva
def add_reserva(session):

    # Chamar função para buscar cliente associado
    from models.cliente import buscar_cliente
    cliente = buscar_cliente(session)

    # Chamar função para buscar funcionário associado
    from models.funcionario import buscar_funcionario
    func = buscar_funcionario(session)

    # Coletar informações da reserva
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE RESERVA')
    print(50 * '=')
    check_in = input("Digite a data de check-in [AAAA-MM-DD HH:MM:SS]: ")
    checkout = input("Digite a data de checkout [AAAA-MM-DD HH:MM:SS]: ")
    descricao = input("Digite a descrição (ex.: Reserva para o Natal): ")
    valor_total = float(input("Digite o valor da reserva: "))

    # Criar uma nova instância de Cliente
    nova_reserva = Reserva(check_in=check_in,
                           checkout=checkout,
                           descricao=descricao,
                           valor_total=valor_total,
                           id_cliente=cliente.id,
                           id_funcionario=func.id)
    
    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'reserva', nova_reserva)


# Função para listar os registros de reserva
def listar_reservas(session):

    reservas = session.query(Reserva).all()

    if not reservas:
        print(50 * "=")
        print("NÃO EXISTEM RESERVAS NO MOMENTO")
        print(50 * "=")    

    else:
        print(50 * '=')
        print('RESERVAS DO HOTEL')
        print(50 * '=')
        verificar_tipo = input("\nDigite o número para listar: \n1. Por cliente \n2. Por funcionário \n3. Todos): ").strip()

        print(50 * "=")
        print("RESERVAS CADASTRADAS")
        print(50 * "=")

        if verificar_tipo == '1':
            # Chamar função para buscar cliente associado
            from models.cliente import buscar_cliente
            cliente = buscar_cliente(session)

            for reserva in reservas:
                if reserva.id_cliente == cliente.id:
                    print(f"\nID Reserva: {reserva.id}\n"
                          f"ID Cliente: {reserva.id_cliente}\n"
                          f"Data de check-in: {reserva.check_in}\n"
                          f"Data de checkout: {reserva.check_out}\n"
                          f"Descrição: {reserva.descricao}\n"
                          f"Valor total: R$ {reserva.valor_total}\n")
                    print(50 * "-")

        elif verificar_tipo == '2':
            # Chamar função para buscar funcionário associado
            from models.funcionario import buscar_funcionario
            func = buscar_funcionario(session)
            
            for reserva in reservas:
                if reserva.id_funcionario == func.id:
                    print(f"\nID Reserva: {reserva.id}\n"
                          f"ID Cliente: {reserva.id_cliente}\n"
                          f"Data de check-in: {reserva.check_in}\n"
                          f"Data de checkout: {reserva.check_out}\n"
                          f"Descrição: {reserva.descricao}\n"
                          f"Valor total: R$ {reserva.valor_total}\n")
                    print(50 * "-")
        
        elif verificar_tipo == '3':
            for reserva in reservas:
                print(f"\nID Reserva: {reserva.id}\n"
                      f"ID Cliente: {reserva.id_cliente}\n"
                      f"Data de check-in: {reserva.check_in}\n"
                      f"Data de checkout: {reserva.check_out}\n"
                      f"Descrição: {reserva.descricao}\n"
                      f"Valor total: R$ {reserva.valor_total}\n")
                print(50 * "-")
            
        else:
            print("Opção inválida!")


# Função para buscar reservas
def buscar_reserva(session):

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_cadastro = solicitar_resposta("Possui reserva no sistema? [S | N]: ")

    if verificar_cadastro == "S":

        # Listar reservas cadastradas
        listar_reservas(session)

        # Selecionar pet por ID
        reserva_id = input("Digite o ID da reserva: ")
        reserva_query = session.query(Reserva).filter(Reserva.id == reserva_id).first()

        # Verifique se a reserva foi encontrada
        if reserva_query:
                print(50 * "=")
                print('RESERVA SELECIONADA')
                print(50 * '-')
                print(f"ID Reserva: {reserva_query.id}")
                print(f"Data de check-in: {reserva_query.check_in}")
                print(f"Data de checkout: {reserva_query.checkout}")
                print(f"Descrição: {reserva_query.descricao}")
                print(50 * '-')

                return reserva_query
        
        else:
            print(50 * '-')
            print("Reserva não encontrada!")

            # Chamar a função para solicitar resposta do usuário a pergunta específica
            question_cadastro = solicitar_resposta("Deseja realizar a reserva? [S | N]:")

            if question_cadastro == "S": return add_reserva(session)
            else: 
                from models.tabelas import executar
                executar()
        
    else: return add_reserva(session)


def executar():
    # Iniciar uma sessão
    from services.db import connection
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar reservas")
        print("2. Adicionar reserva")
        print("3. Buscar reserva")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_reservas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            add_reserva(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            buscar_reserva(session)
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