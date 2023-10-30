def executar():
    while True:
        print(50*"=")
        print("\nSYSTEM - AUNIMAL HOTEL PET \n")
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Funcionário")
        print("4. Profissão")
        print("5. Pet")
        print("6. Raça")
        print("7. Espécie")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import servico
            servico.executar()
        elif escolha == "2":
            # Importe e execute o módulo correspondente aqui
            from . import cliente
            cliente.executar()
        elif escolha == "3":
            # Importe e execute o módulo correspondente aqui
            from . import funcionario
            funcionario.executar()
        elif escolha == "4":
            # Importe e execute o módulo correspondente aqui
            from . import profissao
            profissao.executar()
        elif escolha == "5":
            # Importe e execute o módulo correspondente aqui
            from . import pet
            pet.executar()
        elif escolha == "6":
            # Importe e execute o módulo correspondente aqui
            from . import raca
            raca.executar()
        elif escolha == "7":
            # Importe e execute o módulo correspondente aqui
            from . import especie
            especie.executar()
        
        elif escolha == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()