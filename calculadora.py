import math

def exibir_menu():
    print("\n======= CALCULANK =======")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Porcentagem")
    print("8. Sair")
    print("===========================")

def calculadora():
    while True:
        exibir_menu()
        escolha = input("Escolha uma operação (1-8): ").strip()

        if escolha == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"O resultado da soma é: {num1 + num2}")

        elif escolha == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"O resultado da subtração é: {num1 - num2}")

        elif escolha == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"O resultado da multiplicação é: {num1 * num2}")

        elif escolha == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                print(f"O resultado da divisão é: {num1 / num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")

        elif escolha == "5":
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            print(f"O resultado da potência é: {base ** expoente}")

        elif escolha == "6":
            num = float(input("Digite o número: "))
            if num >= 0:
                print(f"A raiz quadrada de {num} é: {math.sqrt(num)}")
            else:
                print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")

        elif escolha == "7":
            total = float(input("Digite o valor total: "))
            porcentagem = float(input("Digite a porcentagem (%): "))
            print(f"{porcentagem}% de {total} é: {(porcentagem / 100) * total}")

        elif escolha == "8":
            print("Saindo da calculadora. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
