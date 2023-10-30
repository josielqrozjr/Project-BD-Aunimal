from models import Base, Pessoa
from sqlalchemy import DATETIME, VARCHAR, ForeignKey, CHAR, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from datetime import datetime

class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco: Mapped[int] = mapped_column("id_endereco", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    logradouro: Mapped[str] = mapped_column(VARCHAR(50))
    numero:Mapped[SMALLINT] = mapped_column(SMALLINT, nullable=False)
    bairro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    estado: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)


def cadastrar_endereco(session, pessoa_id):
    
    print(50 * "=")
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
    
    try:
        # Adicionar o novo endereco à sessão e fazer o commit para obter o ID gerado
        session.add(novo_endereco)
        session.commit()
            
        # Obter o ID_endereco recém-gerado
        id_endereco = novo_endereco.id_endereco
        print(50 * "=")
        print(f"Dados cadastrados com sucesso. ID Endereço: {id_endereco}")
        print(50 * "=")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao cadastrar endereço: {e}")