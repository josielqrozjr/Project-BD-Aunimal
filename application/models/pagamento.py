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
        print(50 * "=")
        print("O PAGAMENTO JÁ FOI REALIZADO!")
        print(50 * "=")

        from models.funcionario import executar
        executar()        
    
    else:

        # Função para buscar o funcionário associado ao pagamento
        from models.funcionario import buscar_funcionario
        func = buscar_funcionario(session)

        # Coletar dados do novo cadastro em pagamento
        valor = float(input("Digite o valor: "))
        mes_ref = input("Digite o mês referente (ex.: AAAA-MM-DD): ")

        novo_pag = Pagamento(valor=valor,
                             data_pag=datetime.now(),
                             mes_ref=mes_ref,
                             id_funcionario=func.id)

    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(novo_pag)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! ID Funcionário: {novo_pag.id_funcionario}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar pagamento: {e}")
        print(50 * "-")


def excluir_pagamento(session):

    listar_pagamentos(session)
    pag_id = int(input("Digite o ID: "))

    try:
        # Excluir
        session.query(Pagamento).filter(Pagamento.id == pag_id).delete()

        # Confirmar a exclusão
        session.commit()
        print(f"\nRegistro excluído com sucesso. ID pagamento: {pag_id}\n")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"\nErro ao excluir registro de pagamento: {e}\n")