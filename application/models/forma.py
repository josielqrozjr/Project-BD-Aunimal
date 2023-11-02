from models import Base
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Forma(Base):
    __tablename__ = "forma"

    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)

    def __init__(self, descricao):
        self.descricao = descricao


def listar_formas(session):

    formas = session.query(Forma).all()

    if not formas:
        print(50 * "=")
        print("NÃO EXISTEM FORMAS DE COBRANÇA REGISTRADAS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("FORMAS DE COBRANÇA REGISTRADAS")
        print(50 * "=")

        for registro in formas:
            print(f"ID Forma: {registro.id} | Descrição: {registro.descricao}")
     
        print(50 * "-")


def adicionar_forma(session):

    listar_formas(session)

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_cadastro = solicitar_resposta("A forma de cobrança encontra-se na lista acima? (S | N): ")
    
    if verificar_cadastro == 'S':
        forma_id = int(input("Digite o ID da forma de cobrança: "))
        forma = session.query(Forma).filter(Forma.id == forma_id).first()
        
        return forma
    
    else:
        # Coletar dados do novo cadastro em cobrança
        descricao = input("Digite a forma de cobrança (ex.: PIX): ")

        nova_forma = Forma(descricao=descricao)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'forma', nova_forma)