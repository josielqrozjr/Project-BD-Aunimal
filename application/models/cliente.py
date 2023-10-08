from models import Base, Pessoa 
from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime


class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, nullable=False, autoincrement=True, primary_key=True)
    id_pessoa = Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    
    # Relacionamento para acessar os dados de pessoa
    pessoa = relationship('Pessoa', backref='cliente')

    def __init__(self, id_pessoa):
        self.id_pessoa = id_pessoa

 
def listar_clientes(session):  
    # Consultar clientes e seus dados da tabela pessoas com informações combinadas
    dados_clientes = session.query(Cliente, Pessoa).join(Pessoa).all()
    
    for cliente, dadosPessoais in dados_clientes:
        print(f"ID Cliente: {cliente.id_cliente}, Nome: {dadosPessoais.nome}, CPF: {dadosPessoais.cpf}, "
              f"Nascimento: {dadosPessoais.nascimento}, Sexo: {dadosPessoais.sexo}, Email: {dadosPessoais.email}")
        

def adicionar_cliente(session):
    # Coletar informações do associado
    nome = input("Digite o nome do associado: ")
    nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    sexo = input("Digite o sexo (M/F/NI): ").upper
    email = input("Digite o email: ").lower
    est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ").upper
    nacionalidade = input("Digite a nacionalidade: ")
    data_criacao = datetime.now()
    
    # Criar uma nova instância de Associado
    nova_pessoa = Pessoa(nome = nome, 
                         nascimento = nascimento, 
                         cpf = cpf, 
                         rg = rg, 
                         sexo = sexo, 
                         email = email, 
                         est_civil = est_civil, 
                         nacionalidade = nacionalidade, 
                         data_criacao = data_criacao)
    
    try:
        # Adicionar os dados de pessoa a sessão e fazer o commit para obter o ID gerado
        session.add(nova_pessoa)
        session.commit()

        # Obter o ID_pessoa recém-gerado
        id_pessoa = nova_pessoa.id_pessoa

        # Criar uma nova instância de Cliente associando a nova pessoa
        novo_cliente = Cliente(id_pessoa=id_pessoa)
        session.add(novo_cliente)
        session.commit()
        
        print("Cliente adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o cliente: {e}")
