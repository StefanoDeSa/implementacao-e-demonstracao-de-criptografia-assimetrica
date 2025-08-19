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
        print()

    elif opcao == "2":
        try:
            msg = input("Digite a mensagem a ser encriptada: ")
            ciph_b64 = m.criptografar(msg)

            print("\n--- RESULTADO ---")
            print("Texto original:")
            print(msg)
            print("\nTexto encriptado (bytes em Base64):")
            print(ciph_b64)
            print("-----------------\n")

            m.salvar_texto("data/plaintext.txt", msg)
            m.salvar_texto("data/ciphertext.b64", ciph_b64)
            print(">> Arquivos salvos em data/plaintext.txt e data/ciphertext.b64\n")

        except FileNotFoundError:
            print("!! Arquivo de chave pública não encontrado (keys/rsa_pub.pem). Gere chaves na opção [1].\n")
        except Exception as e:
            print(f"!! Erro inesperado: {e}\n")

    elif opcao == "3":
        print(">> Decriptando mensagem...\n")
        try:
            escolha = input("Usar arquivo data/ciphertext.b64? (s/N): ").strip().lower()
            if escolha == "s":
                ciph_b64 = m.ler_texto("data/ciphertext.b64").strip()
            else:
                ciph_b64 = input("Cole o ciphertext em Base64: ").strip()

            plaintext = m.descriptografar(ciph_b64)

            print("\n--- RESULTADO ---")
            print("Texto decriptado (igual ao original):")
            print(plaintext)
            print("-----------------\n")

            m.salvar_texto("data/decrypted.txt", plaintext)
            print(">> Arquivo salvo em data/decrypted.txt\n")

        except FileNotFoundError:
            print("!! Arquivo de chave privada não encontrado (keys/rsa_priv.pem). Gere chaves na opção [1].\n")
            
        except Exception as e:
            print(f"!! Erro inesperado: {e}\n")

    elif opcao == "0":
        print(">> Saindo do programa...")
    else:
        print(">> Opção inválida, tente novamente!\n")
