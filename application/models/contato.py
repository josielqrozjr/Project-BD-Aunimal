from models import Base, Pessoa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, TINYINT


class Contato(Base):
    __tablename__ = "contato"

    codigo_pais: Mapped[int] = mapped_column(TINYINT(3, unsigned=True, zerofill=True), nullable=False)
    codigo_area: Mapped[int] = mapped_column(TINYINT(unsigned=True), nullable=False)
    numero: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, nullable=False)
    id: Mapped[int] = mapped_column("id", INTEGER, ForeignKey(Pessoa.id), primary_key=True, nullable=False)

    
    def __init__(self, codigo_pais, codigo_area, numero, id_pessoa):
        self.codigo_pais = codigo_pais
        self.codigo_area = codigo_area
        self.numero = numero
        self.id = id



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
                           id = pessoa_id)
    
    # Chamar função para inserir cadastro na tabela
    from models.tabelas import inserir_cadastro
    return inserir_cadastro(session, 'contato', novo_contato)