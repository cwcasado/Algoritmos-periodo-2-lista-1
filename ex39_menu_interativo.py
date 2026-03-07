while True:
    print("\n--- MENU DE CADASTRO ---")
    print("1. Adicionar Nome")
    print("2. Ver Lista")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu adicionar!")
        # Seu código de input aqui
    elif opcao == "2":
        print("Exibindo lista...")
        # Seu código de exibição aqui
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break # Quebra o loop e encerra
    else:
        print("Opção inválida! Tente novamente.")
