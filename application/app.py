from models import *
from utils.database_utils import create_db


if __name__ == "__main__":
    print("Criando o Banco de Dados!")
    create_db()


def redirecionar_opcao(opcao):
    if opcao == "1":
        import models.tabelas as modulo
        modulo.executar()
    elif opcao == "2":
        print("Encerrando o programa.")
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        print(50*"=")
        print("\nBem Vindo ao AUNIMAL - Hotel Pet! \n")
        print("\nEscolha uma das opções abaixo: \n")
        print("1. Administrador")
        print("2. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == "2":
            print("Encerrando o programa.")
            break
        else:
            redirecionar_opcao(escolha)
        
if __name__ == "__main__":
    main()