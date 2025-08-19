import module as m


opcao = ""
while opcao != "0":
    m.exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        print(">> Gerando novas chaves...\n")
    elif opcao == "2":
        print(">> Encriptando mensagem...\n")
    elif opcao == "3":
        print(">> Decriptando mensagem...\n")
    elif opcao == "0":
        print(">> Saindo do programa...")
    else:
        print(">> Opção inválida, tente novamente!\n")
