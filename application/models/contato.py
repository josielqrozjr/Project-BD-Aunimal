from models import Base, Pessoa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, TINYINT


class Contato(Base):
    __tablename__ = "contato"

    codigo_pais: Mapped[int] = mapped_column(TINYINT(3, unsigned=True, zerofill=True), nullable=False)
    codigo_area: Mapped[int] = mapped_column(TINYINT(unsigned=True), nullable=False)
    numero: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)

    '''
    def __init__(self, codigo_pais, codigo_area, numero, id_pessoa):
        self.codigo_pais = codigo_pais
        self.codigo_area = codigo_area
        self.numero = numero
        self.id_pessoa = id_pessoa
    '''


def cadastrar_contato(session, pessoa_id):
    
    print(50 * '=')
    print('FORMULÁRIO PARA CADASTRO DE CONTATO')
    print(50 * '=')
    
    codigo_pais = input("Digite o código do país [Brasil: 55]: ")
    codigo_area = input("Digite o DDD: ")
    numero = input("Digite o número: ")

    novo_contato = Contato(codigo_pais = codigo_pais,
                           codigo_area = codigo_area, 
                           numero = numero,
                           id_pessoa = pessoa_id)
    
    try:
        # Adicionar o novo contato à sessão e fazer o commit para obter o ID gerado
        session.add(novo_contato)
        session.commit()
            
        # Obter o ID_endereco recém-gerado
        id_contato_pessoa = novo_contato.id_pessoa

        print(50 * "-")
        print(f"Dados cadastrados com sucesso. ID Pessoa-Contato: {id_contato_pessoa}")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(50 * "-")
        print(f"Erro ao cadastrar contato: {e}")
        print(50 * "-")