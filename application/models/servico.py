from models import Base
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER


class Servico(Base):
    __tablename__ = "servico"
    
    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)

    def __init__(self, valor_total, descricao):
        self.valor_total = valor_total
        self.descricao = descricao


def listar_servicos(session):

    servicos = session.query(Servico).all()

    if not servicos:
        print(50 * "=")
        print("NÃO EXISTEM SERVIÇOS CADASTRADOS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("SERVIÇOS CADASTRADOS")
        print(50 * "=")

        for registro in servicos:
            print(f"\nID Serviço: {registro.id} | Valor: {registro.valor_total}"
                  f"Descrição: {registro.descricao}\n")
        
        print(50 * "-")


def adicionar_servico(session):

    listar_servicos(session)

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_cadastro = solicitar_resposta("O serviço encontra-se na lista acima? (S | N): ")
    
    if verificar_cadastro == 'S':
        servico_id = int(input("Digite o ID do serviço: "))
        servico = session.query(Servico).filter(Servico.id == servico_id).first()
        
        return servico
    
    else:
        # Coletar dados do novo cadastro em serviço
        valor_total = float(input("Digite o valor: "))
        descricao = input("Digite a descrição (ex.: Banho e Tosa): ")

        nova_servico = Servico(valor_total=valor_total,
                               descricao=descricao)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'serviço', nova_servico)