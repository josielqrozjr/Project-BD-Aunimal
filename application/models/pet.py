from models import Base, Especie, Cliente, Raca, Pessoa
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, DATE, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from typing import Literal
import sqlalchemy


Sexo = Literal['M','F']
Porte = Literal['PP', 'P', 'M', 'G', 'GG']

class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(5,2), nullable=True)
    sexo: Mapped[Sexo] = mapped_column(sqlalchemy.Enum('M','F', name="sexo_enum"), nullable=False)
    pelagem: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    porte: Mapped[Porte] = mapped_column(sqlalchemy.Enum('PP', 'P', 'M', 'G', 'GG', name = "porte_enum"), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=True)
    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER, ForeignKey(Especie.id), primary_key=True, nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Cliente.id), nullable=False)


    def __init__(self, data_criacao, nome, peso, sexo, pelagem, 
                 porte, nascimento, descricao, id_especie, id_cliente):
        self.data_criacao = data_criacao
        self.nome = nome
        self.peso = peso
        self.sexo = sexo
        self.pelagem = pelagem
        self.porte = porte
        self.nascimento = nascimento
        self.descricao = descricao
        self.id_especie = id_especie
        self.id_cliente = id_cliente


def listar_pets(session):

    pets = session.query(Pessoa, Cliente, Pet, Raca, Especie).\
        join(Cliente, Pessoa.id == Cliente.id).\
        join(Pet, Cliente.id == Pet.id_cliente).\
        join(Especie, Pet.id_especie == Especie.id).\
        join(Raca, Especie.id_raca == Raca.id).all()

    if not pets:
        print(50 * "=")
        print("NÃO EXISTEM PETS CADASTRADOS")
        print(50 * "=")    

    else:
        print(50 * '=')
        print('PET CADASTRADOS NO HOTEL')
        print(50 * '=')
        verificar_tipo = input("\nEscolha o tipo para listar (GATO | CACHORRO | TODOS): ").strip().upper()

        print(50 * "=")
        print("PETS CADASTRADOS")
        print(50 * "=")

        for registro in pets:
            if verificar_tipo == 'TODOS' or registro.Especie.tipo == verificar_tipo:
                print(f"\nID Pet: {registro.Pet.id}\n"
                      f"Responsável: {registro.Pessoa.nome}\n"
                      f"CPF: {registro.Pessoa.cpf}\n"
                      f"Nome: {registro.Pet.nome}\n"
                      f"Peso: {registro.Pet.peso}\n"
                      f"Sexo: {registro.Pet.sexo}\n"
                      f"Pelagem: {registro.Pet.pelagem}\n"
                      f"Porte: {registro.Pet.porte}\n"
                      f"Nascimento: {registro.Pet.nascimento}\n"
                      f"Descrição: {registro.Pet.descricao}\n"
                      f"Espécie: {registro.Especie.tipo}\n"
                      f"Raça: {registro.Raca.classificacao}\n")
                print(50 * "-")


def adicionar_pet(session):

    # Chamar função para buscar o cliente responsável pelo pet
    from models.cliente import buscar_cliente
    cliente = buscar_cliente(session)

    # Coletar informações do funcionário
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE PET')
    print(50 * '=')

    # Chamar a função para cadastrar/escolher espécie
    from models.especie import adicionar_especie
    especie_pet = adicionar_especie(session)

    # Coletar dados do pet
    nome = input("Digite a nome: ")
    peso = float(input("Digite o peso: "))
    sexo = input("Digite o sexo [M | F]: ")
    pelagem = input("Digite a pelagem (ex.: pelos curtos, brancos): ")
    porte = input("Digite o porte [PP | P | M | G | GG]: ")
    nascimento = input("Digite a data de nascimento [AAAA-MM-DD]: ")
    descricao = input("Digite a descrição (ex.: brincalhão): ")

    # Criar uma nova instância de Pet
    novo_pet = Pet(data_criacao = datetime.now(),
                   nome = nome,
                   peso = peso,
                   sexo = sexo,
                   pelagem = pelagem,
                   porte = porte,
                   nascimento = nascimento,
                   descricao = descricao,
                   id_especie = especie_pet.id,
                   id_cliente = cliente.id)
    
    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'pet', novo_pet)
   

def editar_pet(session):

    print(50 * '=')
    print('ATUALIZAR PET')
    print(50 * '=')

    # Chamar função para buscar o cliente responsável pelo pet
    from models.cliente import buscar_cliente
    cliente = buscar_cliente(session)
    
    try:
        # Buscar pelo ID
        pet_query = session.query(Pet).filter(Pet.id_cliente == cliente.id).one()

        # Exibir o pet atual da pessoa
        print(50 * '=')
        print('PET ENCONTRADO')
        print(50 * '-')
        print(f"\nID Pet: {pet_query.id}\n"
              f"Nome: {pet_query.nome}\n"
              f"Peso: {pet_query.peso}\n"
              f"Sexo: {pet_query.sexo}\n"
              f"Pelagem: {pet_query.pelagem}\n"
              f"Porte: {pet_query.porte}\n"
              f"Nascimento: {pet_query.nascimento}\n"
              f"Descrição: {pet_query.descricao}\n")
        print(50 * '=')

        # Coletar as novas informações de pet
        print(50 * '=')
        print('FORMULÁRIO PARA ATUALIZAR O PET')
        print(50 * '=')

        nome = input("Digite a nome: ")
        peso = float(input("Digite o peso: "))
        sexo = input("Digite o sexo [M | F]: ")
        pelagem = input("Digite a pelagem (ex.: pelos curtos, brancos): ")
        porte = input("Digite o porte [PP | P | M | G | GG]: ")
        nascimento = input("Digite a data de nascimento [AAAA-MM-DD]: ")
        descricao = input("Digite a descrição (ex.: brincalhão): ")

        # Atualizar as informações do pet
        pet_query.nome = nome
        pet_query.peso = peso
        pet_query.sexo = sexo
        pet_query.pelagem = pelagem
        pet_query.porte = porte
        pet_query.nascimento = nascimento
        pet_query.descricao = descricao

        session.commit()
        print(50 * "-")
        print("Pet atualizado com sucesso!")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao editar os dados do pet: {e}")
        print(50 * "-")


# Função para buscar pets
def buscar_pet(session):

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_cadastro = solicitar_resposta("Possui cadastro como pet no sistema? [S | N]: ")

    if verificar_cadastro == "S":

        # Listar pets cadastrados
        listar_pets(session)

        # Selecionar pet por ID
        pet_id = input("Digite o ID do pet: ")
        pet_query = session.query(Pet).filter(Pet.id == pet_id).first()

        # Verifique se o pet foi encontrado
        if pet_query:
                print(50 * "=")
                print('PET SELECIONADO')
                print(50 * '-')
                print(f"ID Pet: {pet_query.id}")
                print(f"Nome: {pet_query.nome}")
                print(50 * '-')

                return pet_query
        
        else:
            print(50 * '-')
            print("Cadastro de pet não encontrado!")

            # Chamar a função para solicitar resposta do usuário a pergunta específica
            question_cadastro = solicitar_resposta("Deseja realizar o cadastro? [S | N]:")

            if question_cadastro == "S": return adicionar_pet(session)
            else: 
                from models.tabelas import executar
                executar()
        
    else: return adicionar_pet(session)


def executar():
    # Iniciar uma sessão
    from services.db import connection
    session = connection

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar pets")
        print("2. Adicionar pet")
        print("3. Editar pet")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_pets(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_pet(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_pet(session)
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