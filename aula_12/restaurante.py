cardapio = ["Salada", "Macarronada", "Sanduiche", "Sorvete"]


def cumprimentar():
    print("Bem-vindo ao restaurante!")
    print("Escolha uma das opções abaixo:")

def restaurante():

    while True:
        print("\nCARDÁPIO:")

        for i in range(4):
            print(i + 1, "-", cardapio[i])

        print("0 - Sair")

        opcao = int(input("Digite o número da opção: "))

        if opcao == 1:
            print("Você escolheu Salada.")

        elif opcao == 2:
            print("Você escolheu Macarronada.")

        elif opcao == 3:
            print("Você escolheu Sanduiche.")

        elif opcao == 4:
            print("Você escolheu Sorvete.")

        elif opcao == 0:
            print("Obrigado pela preferência!")
            break

        else:
            print("Opção inválida!")


cumprimentar()
restaurante()