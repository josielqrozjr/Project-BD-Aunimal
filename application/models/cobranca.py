from models import Base, Funcionario, Reserva
from sqlalchemy import DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime

class Cobranca(Base):
    __tablename__ = "cobranca"

    id: Mapped[int] = mapped_column("id", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_cobranca: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id), nullable=False)

    def __init__(self, data_cobranca, valor_total, id_reserva, id_funcionario):
        self.data_cobranca = data_cobranca
        self.valor_total = valor_total
        self.id_reserva = id_reserva
        self.id_funcionario = id_funcionario


def listar_cobrancas(session):

    cobrancas = session.query(Cobranca).all()

    if not cobrancas:
        print(50 * "=")
        print("NÃO EXISTEM COBRANÇAS REGISTRADAS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("COBRANÇAS REGISTRADAS")
        print(50 * "=")

        for registro in cobrancas:
            print(f"\nID Cobrança: {registro.id}\n"
                  f"Data da cobrança: {registro.data_cobranca}\n"
                  f"Valor: {registro.valor_total}\n"
                  f"ID Reserva: {registro.id_reserva}\n"
                  f"ID Funcionário: {registro.classificacao}\n")
                  
        print(50 * "-")


def adicionar_cobranca(session):

    listar_cobrancas(session)

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_cadastro = solicitar_resposta("A cobrança encontra-se na lista acima? (S | N): ")
    
    if verificar_cadastro == 'S':
        cobranca_id = int(input("Digite o ID da cobrança: "))
        cobranca = session.query(Cobranca).filter(Cobranca.id == cobranca_id).first()
        
        return cobranca
    
    else:
        # Coletar dados do novo cadastro em cobrança
        data_cobranca = input("Digite a data da cobrança [AAAA-MM-DD HH:MM:SS]: ")
        valor_total = float(input("Digite o valor total: "))

        # Chamar funções para cadastrar/escolher funcionário e reserva
        from models.reserva import buscar_reserva
        reserva = buscar_reserva(session)

        from models.funcionario import buscar_funcionario
        func = buscar_funcionario(session)

        nova_cobranca = Cobranca(data_cobranca=data_cobranca,
                                 valor_total=valor_total,
                                 id_reserva=reserva.id,
                                 id_funcionario=func.id)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'cobrança', nova_cobranca)