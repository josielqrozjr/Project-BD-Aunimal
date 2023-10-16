def executar():
    while True:
        print(50*"=")
        print("")
        print("TELA ADM")
        print("")
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Funcionario")
        print("4. Profissao")
        print("5. pet")
        print("6. raca")
        print("7. especie")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import tb_servico
            tb_servico.executar()
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
            from . import tb_profissao
            tb_profissao.executar()
        elif escolha == "5":
            # Importe e execute o módulo correspondente aqui
            from . import tb_pet
            tb_pet.executar()
        elif escolha == "6":
            # Importe e execute o módulo correspondente aqui
            from . import tb_raca
            tb_raca.executar()
        elif escolha == "7":
            # Importe e execute o módulo correspondente aqui
            from . import tb_especie
            tb_especie.executar()
        
        elif escolha == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()