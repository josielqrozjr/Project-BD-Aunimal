def inserir_cadastro(session, nome_tabela, dados):
    try:
        # Adicionar os dados à sessão e fazer o commit
        session.add(dados)
        session.commit()

        print(50 * "-")
        print(f"\nDados cadastrados com sucesso! ID {nome_tabela}: {dados.id}")
        print(50 * "-")

        return dados

    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        
        print(50 * "-")
        print(f"Erro ao cadastrar {nome_tabela}: {e}")
        print(50 * "-")

        executar()


# Função para solicitar e verficar uma resposta com resultados de S e N
def solicitar_resposta(pergunta):
    print("")
    resposta = input(pergunta).strip().upper()

    while resposta != 'S' and resposta != 'N':
        print("\nComando inválido! Digite novamente.")
        resposta = input(pergunta).strip().upper()

    return resposta



def executar():
    while True:
        print(50*"=")
        print("\nSYSTEM - AUNIMAL HOTEL PET \n")
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Funcionários")
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