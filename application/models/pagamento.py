from models import Base, Funcionario
from sqlalchemy import DATETIME, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    data_pag: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    mes_ref: Mapped[date] = mapped_column(DATE, nullable=False, primary_key=True)
    id_funcionario: Mapped[int] = mapped_column("id", INTEGER, ForeignKey(Funcionario.id), primary_key=True, nullable=False)

    def __init__(self, valor, data_pag, mes_ref, id_funcionario):
        self.valor = valor
        self.data_pag = data_pag
        self.mes_ref = mes_ref
        self.id_funcionario = id_funcionario


def listar_pagamentos(session):

    pagamentos = session.query(Pagamento).all()

    if not pagamentos:
        print(50 * "=")
        print("NÃO EXISTEM PAGAMENTOS REALIZADOS")
        print(50 * "=")

    else:
        print(50 * "=")
        print("PAGAMENTOS REALIZADOS")
        print(50 * "=")

        for registro in pagamentos:
            print(f"\nID Funcionário: {registro.id_funcionario}\n"
                  f"Valor: {registro.valor_total}\n"
                  f"Data do pagamento: {registro.mes_ref}\n"
                  f"Mês: {registro.valor_total}\n")
        
        print(50 * "-")


def adicionar_pagamento(session):

    listar_pagamentos(session)

    # Chamar a função para solicitar resposta do usuário a pergunta específica
    from models.tabelas import solicitar_resposta
    verificar_registro = solicitar_resposta("O pagamento encontra-se na lista acima? (S | N): ")
    
    if verificar_registro == 'S':
        pag_id = int(input("Digite o ID do funcionário: "))
        pagamento = session.query(Pagamento).filter(Pagamento.id == pag_id).first()
        
        return pagamento
    
    else:
        # Coletar dados do novo cadastro em pagamento
        valor = float(input("Digite o valor: "))
        mes_ref = input("Digite o mês referente (ex.: AAAA-MM-DD): ")

        # Função para buscar o funcionário associado ao pagamento
        from models.funcionario import buscar_funcionario
        func = buscar_funcionario(session)

        novo_pag = Pagamento(valor=valor,
                             data_pag=datetime.now(),
                             mes_ref=mes_ref,
                             id_funcionario=func.id)

        # Chamar função para inserir cadastro na tabela
        from models.tabelas import inserir_cadastro
        return inserir_cadastro(session, 'pagamento', novo_pag)