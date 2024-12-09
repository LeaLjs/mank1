import time
import os

print("Seja Bem Vindo(a) Essa é a versão 1.0.0 Do Mank Os!")
print("Digite 'menu' para ver a lista de comandos, 'apps' para ver a lista de aplicativos ou 'help' para um guia completo de como usar o Mank.")

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

# Loop principal do terminal
while True:
    
    os.system("color 02")
    print("\033[H\033[J", end="")
    print(r" __  __    _    _   _ _  ___    ___  ____  ")
    print(r"|  \/  |  / \  | \ | | |/ / |  / _ \/ ___| ")
    print(r"| |\/| | / _ \ |  \| | ' /| | | | | \___ \ ")
    print(r"| |  | |/ ___ \| |\  | . \|_| | |_| |___) |")
    print(r"|_|  |_/_/   \_\_| \_|_|\_(_)  \___/|____/ ")
    print(r" _   ___   ___  ")
    print(r"/ | / _ \ / _ \ ")
    print(r"| || | | | | | |")
    print(r"| || |_| | |_| |")
    print(r"|_(_)___(_)___/ ")
    #for i in range(1):
    #             print("Carregando...")
    #             time.sleep(5)
    #print("50% pronto");
    #for i in range(1):
    #             print("Quase lá...")
    #             time.sleep(5)
    #print("Carregado");

# Exibe a mensagem de boas-vindas
    print("Seja Bem Vindo(a) Essa é a versão 1.0.0 Do Mank Os!")
    print("Digite 'menu' para ver a lista de comandos, 'apps' para ver a lista de aplicativos ou 'help' para um guia completo de como usar o Mank.")
    comandInput = input("C:\\> ").strip().lower()  # Transforma o input para minúsculas

    if comandInput == "":
        print("Você não escreveu nada. Tente novamente.")

    elif comandInput == "menu":
        print("Bem Vindo Ao Menu do Mank")
        print("==================================(COMANDOS PRINCIPAIS)==================================")
        print("1. sudo - Instala Aplicativos")
        print("2. mank --V - Mostra a Versão do Mank ")
        print("3. mkdir - Cria Uma Pasta")
        print("4. cd - Abre Uma Pasta")
        print("5. date - Mostra A data dia e ano")
        print("6. help - Exibe uma mensagem de ajuda")
        print("7. whiteHat - te Dá o Controle Total")
        print("8. sair - Fecha o Mank :(")

    elif comandInput == "apps":
        print("Mank Store ;)")
        print("==================================(Jogos)==================================")
        print("Formula 1 code:#00g1")
        print("Cross Frog code:#00g2")
        print("Flying Wars code:#00g3")
        print("Avoid the Wall code:#00g4")
        print("==================================(Apps)==================================")
        print("Explorador de arquivos")
        print("Mank Bash")
        print("Mankode Editor")
        print("Calculadora")

        print("como instalar:")
        print("Use o Comando Sudo e o Nome do aplicativo Ex:")
        print("sudo formula 1,sudo Mank Bash, Lembre-se De Escrever O Nome Exatamente igual e com letras minúsculas,caso contrário o programa não vai funcionar")

    elif comandInput == "help":
        print("========================(Guia de comandos)========================")
        print("menu - Exibe o menu de comandos principais")
        print("apps - Exibe a lista de jogos e aplicativos disponíveis")
        print("help - Exibe esta mensagem de ajuda")
        print("clear - Limpa a tela")
        print("sair - Fecha o terminal")

    elif comandInput == "mkdir":
        nome_pasta = input("Digite o nome da nova pasta: ").strip()
        if not os.path.exists(nome_pasta):
            os.mkdir(nome_pasta)
            print(f"\nPasta '{nome_pasta}' criada com sucesso!")
        if os.payt.exist(nome_pasta):
            print("Esta pasta já existe")
        

    elif comandInput == "date":
        from datetime import datetime
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Data e hora atual: {data_hora_atual}")

    
    elif comandInput == "cd":
        itens = os.listdir()
        if itens:
                print("\nConteúdo do diretório:")
                for item in itens:
                    print(f"  - {item}")
        else:
                print("\nO diretório está vazio.")

    elif comandInput == "sair":
        print("Saindo do terminal... Até logo!")
        break  # Sai do loop principal

    elif comandInput == "mank --v" or comandInput == "mank version" or comandInput == "mank --version":
        print("mank 1.0.0 ")
    
    elif comandInput == "clear":
        print("\033[H\033[J", end="")  # Comando para limpar a tela no terminal
    #Baixar e Rodar o Formula 1
    elif comandInput == "sudo formula1" or comandInput == "sudo formula 1":
        for i in range(10):
            print("Baixando Formula 1...", end="\r")
            time.sleep(1)
        print("Formula 1 Instalado, Para Jogar digíte sud'run #00g1'")

    #Baixar e Rodar o Cross Frog
    elif comandInput == "sudo cross frog" or comandInput == "sudo crossfrog" or comandInput == "sudocross frog":
        for i in range(10):
            print("Baixando Cross Frog ...", end="\r")
            time.sleep(1)
        print("Cross frog instalado, Para Jogar digíte 'run #00g1'")

    #Baixar e Rodar o Flying Wars
    elif comandInput == "sudo flying wars" or comandInput == "sudo flyingwars" or comandInput == "sudoflywars" or comandInput == "sudo fw":
        for i in range(10):
            print("Baixando Flying Wars...", end="\r")
            time.sleep(1)
        print("Flying Wars Instalado, Para Jogar digíte 'run flyin wars ou fly wars '")

    #Baixar e Rodar o Avoid The Wall
    elif comandInput == "sudo #00g4":
        for i in range(10):
            print("Baixando Avoid The Wall...", end="\r")
            time.sleep(1)
        print(" Avoid the Wall Instalado, Para Jogar digíte 'run #00g1'")

    #Baixar e Rodar o Mank Explorer
    elif comandInput == "sudo explorer":
           for i in range(1):
            print("Baixando Mank Explorer...", end="\r")
            time.sleep(8)
            print("Mank Explorer instalados, Para Usar digíte 'run #00ap1'");
    elif comandInput == "run explorer":
                print("Abrindo o Gerenciador de Arquivos...")
                gerenciador_arquivos()
               

    #Baixar e Rodar o Mank Bash
    elif comandInput == "sudo mank bash":
         for i in range(1):
            print("Baixando Mank Bash...", end="\r")
            time.sleep(8)
            print("Mank Explorer instalados, Para Usar digíte 'run #00ap2'");
    elif comandInput == "run mank bash":
                print("Abrindo o Mank Bash...")
                
    
    # Baixar E Rodar O Mankode 
    elif comandInput == "sudo mankode":
            for i in range(1):
                print("Baixando Mankode Editor...", end="\r")
            time.sleep(8)
            print("Mankode Editor instalado, Para Usar digíte 'run #00ap3'");
    elif comandInput == "run mankode":
        print("Abrindo o editor de texto...")
        import subprocess
        subprocess.run(["python", "mankode_editor.py"])  # Nome do arquivo do editor
    
    elif comandInput == "sudo calculadora":
            for i in range(1):
                print("Baixando Calculadora Mank...", end="\r")
            time.sleep(8)
            print("Calculadora instalada, Para Usar digíte 'run #00ap3'");
    elif comandInput == "run calculadora":
        print("Abrindo Calculadora...")
        import subprocess
        subprocess.run(["python", "mankode_editor.py"])  # Nome do arquivo do editor

    elif comandInput == "whitehat":
        print("\033[H\033[J", end="")  # Comando para limpar a tela no terminal
        import os
        os.system("color1E")
        comandInput = input("~$ ").strip().lower()

    else:
        print(f"Comando '{comandInput}' não reconhecido. Digite 'help' para ver a lista de comandos.")