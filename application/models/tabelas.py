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
        print("8. Endereço")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import servico
            servico.executar()

        elif escolha == "2":
            from . import cliente
            cliente.executar()

        elif escolha == "3":
            from . import funcionario
            funcionario.executar()

        elif escolha == "4":
            from . import profissao
            profissao.executar()

        elif escolha == "5":
            from . import pet
            pet.executar()

        elif escolha == "6":
            from . import raca
            raca.executar()

        elif escolha == "7":
            from . import especie
            especie.executar()

        elif escolha == "8":
            from . import endereco
            endereco.executar()
        
        elif escolha == "9":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()