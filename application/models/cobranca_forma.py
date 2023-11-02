from models import Base, Cobranca, Forma
from sqlalchemy import DECIMAL, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Cobranca_forma(Base):
    __tablename__ = "cobranca_forma"

    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    parcela: Mapped[str] = mapped_column(VARCHAR(45), nullable=True)
    id_cobranca: Mapped[int] = mapped_column("id_cobranca", INTEGER,ForeignKey(Cobranca.id), primary_key=True, nullable=False)
    id_forma: Mapped[int] = mapped_column("id_forma", INTEGER,ForeignKey(Forma.id), primary_key=True, nullable=False)

    def __init__(self, valor, parcela, id_cobranca, id_forma):
        self.valor = valor
        self.parcela = parcela
        self.id_cobranca = id_cobranca
        self.id_forma = id_forma


def add_cobranca_forma(session):

    # Chamar funções para buscar/cadastrar cobrança e forma
    from models.cobranca import adicionar_cobranca
    cobranca = adicionar_cobranca(session)

    from models.forma import adicionar_forma
    forma = adicionar_forma(session)

    # Coletar dados para cadastro
    valor = float(input("Digite o valor: R$ "))
    parcela = input("Digite a parcela (ex.: 12 vezes, à vista): ")

    nova_cobran_form = Cobranca_forma(valor=valor,
                                      parcela=parcela,
                                      id_cobranca=cobranca.id,
                                      id_forma=forma.id)
    
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(nova_cobran_form)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! \nID Cobrança: {nova_cobran_form.id_cobranca} ID Forma: {nova_cobran_form.id_forma}\n")
        print(50 * "-")

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar cobrança-forma: {e}")
        print(50 * "-")