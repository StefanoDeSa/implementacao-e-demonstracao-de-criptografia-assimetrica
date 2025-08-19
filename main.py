import module as m


opcao = ""
while opcao != "0":
    m.exibir_menu()
    opcao = input(">> Opção: ")

    if opcao == "1":
        print(">> Gerando novas chaves...\n")

        info = m.gerar_e_salvar_chaves()
        print(">> Chaves geradas com sucesso!")
        print(f"   Privada: {info['private_key_path']}")
        print(f"   Pública: {info['public_key_path']}")
        
    elif opcao == "2":
        print(">> Encriptando mensagem...\n")
    elif opcao == "3":
        print(">> Decriptando mensagem...\n")
    elif opcao == "0":
        print(">> Saindo do programa...")
    else:
        print(">> Opção inválida, tente novamente!\n")
