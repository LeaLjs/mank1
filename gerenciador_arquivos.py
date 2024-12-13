import os
def gerenciador_arquivos():
    while True:
        print("\n========= GERENCIADOR DE ARQUIVOS =========")
        print(f"Diretório atual: {os.getcwd()}")
        print("1. Listar arquivos e pastas")
        print("2. Navegar para outro diretório")
        print("3. Criar uma nova pasta")
        print("4. Criar um novo arquivo")
        print("5. Apagar um arquivo")
        print("6. Apagar uma pasta")
        print("7. Voltar ao diretório anterior")
        print("8. Sair do gerenciador")
        print("===========================================")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            itens = os.listdir()
            if itens:
                print("\nConteúdo do diretório:")
                for item in itens:
                    print(f"  - {item}")
            else:
                print("\nO diretório está vazio.")

        elif escolha == "2":
            destino = input("Digite o caminho do diretório: ").strip()
            if os.path.isdir(destino):
                os.chdir(destino)
                print(f"\nAgora você está em: {os.getcwd()}")
            else:
                print("\nDiretório não encontrado!")

        elif escolha == "3":
            nome_pasta = input("Digite o nome da nova pasta: ").strip()
            if not os.path.exists(nome_pasta):
                os.mkdir(nome_pasta)
                print(f"\nPasta '{nome_pasta}' criada com sucesso!")
            else:
                print("\nUma pasta com esse nome já existe.")

        elif escolha == "4":
            nome_arquivo = input("Digite o nome do arquivo (ex: arquivo.txt): ").strip()
            if not os.path.exists(nome_arquivo):
                with open(nome_arquivo, "w") as arquivo:
                    arquivo.write("")
                print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")
            else:
                print("\nUm arquivo com esse nome já existe.")

        elif escolha == "5":
            nome_arquivo = input("Digite o nome do arquivo para apagar: ").strip()
            if os.path.isfile(nome_arquivo):
                os.remove(nome_arquivo)
                print(f"\nArquivo '{nome_arquivo}' apagado com sucesso!")
            else:
                print("\nArquivo não encontrado!")

        elif escolha == "6":
            nome_pasta = input("Digite o nome da pasta para apagar: ").strip()
            if os.path.isdir(nome_pasta):
                try:
                    os.rmdir(nome_pasta)
                    print(f"\nPasta '{nome_pasta}' apagada com sucesso!")
                except OSError:
                    print("\nA pasta não está vazia. Não pode ser apagada.")
            else:
                print("\nPasta não encontrada!")

        elif escolha == "7":
            os.chdir("..")
            print(f"\nAgora você está em: {os.getcwd()}")

        elif escolha == "8":
            print("\nSaindo do gerenciador de arquivos. Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
