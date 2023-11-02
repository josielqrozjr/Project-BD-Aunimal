from models import Base, Pessoa
from sqlalchemy import DATETIME, VARCHAR, ForeignKey, CHAR, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from datetime import datetime
from services.db import connection


class Endereco(Base):
    __tablename__ = "endereco"

    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    logradouro: Mapped[str] = mapped_column(VARCHAR(50))
    numero:Mapped[SMALLINT] = mapped_column(SMALLINT, nullable=False)
    bairro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    estado: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id), primary_key=True, nullable=False)


def cadastrar_endereco(session, pessoa_id):
    
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE ENDEREÇO')
    print(50 * '=')

    cep = input("Digite o CEP: ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    novo_endereco = Endereco(data_criacao = datetime.now(), 
                             cep = cep,
                             logradouro = logradouro,
                             numero = numero,
                             bairro = bairro,
                             cidade = cidade,
                             estado = estado,
                             id_pessoa = pessoa_id)
    
    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'endereço', novo_endereco)


def editar_endereco(session):

    print(50 * '=')
    print('ATUALIZAR ENDEREÇO')
    print(50 * '=')

    #Chamar a função para identificar a pessoa correspondente
    from models.pessoa import buscar_pessoa
    pessoa = buscar_pessoa(session)
    
    try:
        # Buscar pelo ID
        endereco_pessoa = session.query(Endereco).filter(Endereco.id_pessoa == pessoa.id).one()

        # Exibir o endereço atual da pessoa
        print(50 * '=')
        print('ENDEREÇO ENCONTRADO')
        print(50 * '-')
        print(f"ID Pessoa: {endereco_pessoa.id_pessoa}")
        print(f"CEP: {endereco_pessoa.cep}")
        print(f"Logradouro: {endereco_pessoa.logradouro}")
        print(f"Número: {endereco_pessoa.numero}")
        print(f"Bairro: {endereco_pessoa.bairro}")
        print(f"Cidade: {endereco_pessoa.cidade}")
        print(f"Estado: {endereco_pessoa.estado}")
        print(50 * '=')

        # Coletar as novas informações de endereço
        print(50 * '=')
        print('FORMULÁRIO PARA ATUALIZAR O ENDEREÇO')
        print(50 * '=')

        cep = input("Digite o CEP: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite o estado: ")

        # Atualizar as informações da pessoa
        endereco_pessoa.cep = cep
        endereco_pessoa.logradouro = logradouro
        endereco_pessoa.numero = numero
        endereco_pessoa.bairro = bairro
        endereco_pessoa.cidade = cidade
        endereco_pessoa.estado = estado

        session.commit()
        print(50 * "-")
        print("Endereço atualizado com sucesso!")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao editar o endereço: {e}")
        print(50 * "-")


def listar_enderecos(session):

    enderecos = session.query(Endereco).all()

    if not enderecos:
        print(50 * "=")
        print("NÃO EXISTEM ENDEREÇOS REGISTRADOS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("ENDEREÇOS REGISTRADOS")
        print(50 * "=")

        for registro in enderecos:
            print(f"ID Endereço: {registro.id}\n"
                  f"ID Pessoa: {registro.id_pessoa}")
     
        print(50 * "-")


def excluir_endereco(session):

    listar_enderecos(session)
    endereco_id = int(input("Digite o ID: "))

    try:
        # Excluir
        session.query(Endereco).filter(Endereco.id == endereco_id).delete()

        # Confirmar a exclusão
        session.commit()
        print(f"\nRegistro excluído com sucesso. ID endereço: {endereco_id}\n")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"\nErro ao excluir registro de endereço: {e}\n")
    


def executar():
    # Iniciar uma sessão
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Editar endereço")
        print("2. Excluir endereço")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            editar_endereco(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            excluir_endereco(session)
        elif escolha == "3":
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