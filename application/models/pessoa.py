from models import Base
from sqlalchemy import DATETIME, DATE, VARCHAR, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from typing import Literal
import sqlalchemy


Sexo = Literal['M','F','NI']
Est_civil = Literal['SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO']

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id: Mapped[int] = mapped_column("id", INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    sexo: Mapped[Sexo] = mapped_column(sqlalchemy.Enum('M','F','NI', name="sexo_enum"), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    est_civil: Mapped[Est_civil] = mapped_column(sqlalchemy.Enum('SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO', name = "est_civil_enum"), nullable=False)
    nacionalidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, default='BRASIL')
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    
    def __init__(self, nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao):
       self.nome = nome
       self.nascimento = nascimento
       self.cpf = cpf
       self.rg = rg
       self.sexo = sexo 
       self.email = email 
       self.est_civil = est_civil
       self.nacionalidade = nacionalidade
       self.data_criacao = data_criacao


# Listar as pessoas que estão associadas a tabela passada no parâmetro
def listar_pessoa(session, pessoa_id):
    
    # Consultar pessoas e atribuir os resultados na variável
    dados_pessoa = session.query(Pessoa).filter(Pessoa.id == pessoa_id)
    
    for pessoa in dados_pessoa:
        print(50 * "=")
        print(f"\nNome: {pessoa.nome}" 
              f"\nData de nascimento: {pessoa.nascimento}"
              f"\nCPF: {pessoa.cpf}"
              f"\nRG: {pessoa.rg}"
              f"\nSexo: {pessoa.sexo}"
              f"\nEstado Civil: {pessoa.est_civil}"
              f"\nNacionalidade: {pessoa.nacionalidade}"
              f"\nEmail: {pessoa.email}")
        

# Função para buscar pessoa pelo CPF
def buscar_pessoa(session):

    # Perguntar se possui cadastro
    verificar_cadastro = input("Possui dados pessoais cadastrados no sistema? [S | N]: ").strip().lower()

    if verificar_cadastro == "s":

        # Consultar pessoa por CPF
        cpf_pessoa = input("Digite o CPF para consultar: ")
        pessoa_query = session.query(Pessoa).filter(Pessoa.cpf == cpf_pessoa).first()

        # Verifique se a pessoa foi encontrada
        if pessoa_query:
            print(50 * "=")
            print('PESSOA ENCONTRADA')
            print(50 * '-')
            print(f"ID Pessoa: {pessoa_query.id}")
            print(f"Nome: {pessoa_query.nome}")
            print(f"Nascimento: {pessoa_query.nascimento}")
            print(f"CPF: {pessoa_query.cpf}")
            print(f"RG: {pessoa_query.rg}")
            print(f"Sexo: {pessoa_query.sexo}")
            print(f"Email: {pessoa_query.email}")
            print(f"Estado Civil: {pessoa_query.est_civil}")
            print(f"Nacionalidade: {pessoa_query.nacionalidade}")
            print(50 * '=')

            return pessoa_query
    
        else:
            print(50 * '=')
            print("Cadastro não encontrado!")
            question_cadastro = input("Deseja realizar o cadastro? [S | N]:").strip().lower()

            if question_cadastro == "s": return cadastrar_pessoa(session)
            else: 
                from models.tabelas import executar
                executar()
        
    else: return cadastrar_pessoa(session)
    

# Função para cadastrar dados da pessoa
def cadastrar_pessoa(session):
    
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE PESSOA')
    print(50 * '=')

    # Coletar dados do novo cadastro em pessoa
    nome = input("Digite o nome: ")
    nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")

    # Verificar o CPF
    while True:
        cpf = input("Digite o CPF (11 dígitos): ")
        if len(cpf) == 11 and cpf.isdigit():
            break
        else:
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")

    rg = input("Digite o RG: ")
    sexo = input("Digite o sexo (M | F | NI): ")
    email = input("Digite o email: ")
    est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
    nacionalidade = input("Digite a nacionalidade: ")
        
    # Criar uma nova instância de Pessoa
    nova_pessoa = Pessoa(nome = nome, 
                        nascimento = nascimento, 
                        cpf = cpf, 
                        rg = rg, 
                        sexo = sexo, 
                        email = email, 
                        est_civil = est_civil, 
                        nacionalidade = nacionalidade, 
                        data_criacao = datetime.now())
        
    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    cadastrar = inserir_cadastro(session, 'pessoa', nova_pessoa)

    # Chamar função para cadastrar endereço
    from models.endereco import cadastrar_endereco
    cadastrar_endereco(session, cadastrar.id)

    # Chamar função para cadastrar contato
    from models.contato import cadastrar_contato
    cadastrar_contato(session, cadastrar.id)

    return cadastrar


# Função para editar dados da pessoa
def editar_pessoa(session):
        
    print(50 * '=')
    print('ATUALIZAR DADOS PESSOAIS')
    print(50 * '=')

    #Chamar a função para identificar a pessoa correspondente
    dados_pessoais = buscar_pessoa(session)

    try:

        # Coletar as novas informações da pessoa
        print(50 * '=')
        print('FORMULÁRIO PARA ATUALIZAR DADOS PESSOAIS')
        print(50 * '=')

        nome = input("Digite o novo nome da pessoa: ")
        nascimento = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
        cpf = input("Digite o novo CPF: ")
        rg = input("Digite o novo RG: ")
        sexo = input("Digite o novo sexo (M | F | NI): ")
        email = input("Digite o novo email: ")
        est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
        nacionalidade = input("Digite a nova nacionalidade: ")

        # Atualizar as informações da pessoa
        dados_pessoais.nome = nome
        dados_pessoais.nascimento = nascimento
        dados_pessoais.cpf = cpf
        dados_pessoais.rg = rg
        dados_pessoais.sexo = sexo
        dados_pessoais.email = email
        dados_pessoais.est_civil = est_civil
        dados_pessoais.nacionalidade = nacionalidade

        session.commit()
        print(50 * '-')
        print("Dados pessoais atualizados com sucesso!")
        print(50 * '-')

        return dados_pessoais

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao atualizar os dados pessoais: {e}")
        print(50 * "-")