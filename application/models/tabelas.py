from services.db import connection


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
        print("1.  Clientes")
        print("2.  Funcionários")
        print("3.  Endereço")
        print("4.  Reservas")
        print("5.  Pet")
        print("6.  Cadastro fácil: Pet e Reserva")
        print("7.  Cadastro fácil: Pet e Serviço")
        print("8.  Cadastro fácil: Reserva e Serviço")
        print("9. Cadastro fácil: Funcionário e Serviço")
        print("10. Cadastro fácil: Cobrança e Forma")
        print("11. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Importa e executa o módulo correspondente
            from . import cliente
            cliente.executar()

        elif escolha == "2":
            from . import funcionario
            funcionario.executar()

        elif escolha == "3":
            from . import endereco
            endereco.executar()

        elif escolha == "4":
            from . import reserva
            reserva.executar()

        elif escolha == "5":
            from . import pet
            pet.executar()

        elif escolha == "6":
            from . import pet_reserva
            pet_reserva.add_pet_reserva(connection)

        elif escolha == "7":
            from . import pet_servico
            pet_servico.add_pet_servico(connection)

        elif escolha == "8":
            from . import reserva_servico
            reserva_servico.add_reserva_serv(connection)

        elif escolha == "9":
            from . import funcionario_servico
            funcionario_servico.add_func_servico(connection)

        elif escolha == "10":
            from . import cobranca_forma
            cobranca_forma.add_cobranca_forma(connection)
        
        elif escolha == "11":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()