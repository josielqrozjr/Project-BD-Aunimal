from models import Base
from sqlalchemy import DATETIME, DATE, VARCHAR, CHAR, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from typing import Literal
import sqlalchemy


Sexo = Literal['M','F','NI']
Est_civil = Literal['SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO']

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    sexo: Mapped[Sexo] = mapped_column(sqlalchemy.Enum('M','F','NI', name="sexo_enum"), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    est_civil: Mapped[Est_civil] = mapped_column(sqlalchemy.Enum('SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO', name = "est_civil_enum"), nullable=False)
    nacionalidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, default='BRASIL')
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    
    '''def __init__(self, nome, nascimento, cpf, rg, sexo, email, est_civil, nacionalidade, data_criacao):
       self.nome = nome
       self.nascimento = nascimento
       self.cpf = cpf
       self.rg = rg
       self.sexo = sexo 
       self.email = email 
       self.est_civil = est_civil
       self.nacionalidade = nacionalidade
       self.data_criacao = data_criacao'''


# Listar as pessoas que estão associadas a tabela passada no parâmetro
def listar_pessoa(session, id):
    
    # Consultar pessoas e atribuir os resultados na variável
    dados_pessoa = session.query(Pessoa).filter(Pessoa.id_pessoa == id)
    
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
    verificar_cadastro = input("A pessoa já possui cadastro no sistema? (S/N): ").strip().lower()

    if verificar_cadastro == "s":
        # Coletar informações já existentes
        #cpf_pessoa = input("Digite o CPF para consultar: ")
        #pesq_cadastro = session.query(Pessoa).filter_by(cpf = cpf_pessoa).first()

        cpf_pessoa = input("Digite o CPF para consultar: ")
    
        # Consultar pessoa por CPF
        pessoa_query = session.query(Pessoa).filter(Pessoa.cpf == cpf_pessoa).first()

        # Verifique se a pessoa foi encontrada
        if pessoa_query:
            id_pessoa = pessoa_query.id_pessoa
            print(50 * "=")
            print(f"ID Pessoa: {pessoa_query.id_pessoa}")
            print(f"Nome: {pessoa_query.nome}")
            print(50 * "=")

            return id_pessoa
    
        else:
            print(50 * '=')
            print("Cadastro não encontrado!")

            return cadastrar_pessoa(session)
        
    else: return cadastrar_pessoa(session)
    

# Função para cadastrar pessoa
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
    sexo = input("Digite o sexo (M/F/NI): ")
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
        
    try:
        # Adicionar o novo cadastro à sessão e fazer o commit para obter o ID gerado
        session.add(nova_pessoa)
        session.commit()

        # Obter o ID_pessoa recém-gerado
        id_gerado = nova_pessoa.id_pessoa

        # Chamar função para cadastrar endereço
        from models.endereco import cadastrar_endereco
        cadastrar_endereco(session, id_gerado)

        print(50 * "=")
        print(f"Dados cadastrados com sucesso. ID Pessoa: {id_gerado}")
        return id_gerado
        
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao cadastrar os dados pessoais: {e}")
