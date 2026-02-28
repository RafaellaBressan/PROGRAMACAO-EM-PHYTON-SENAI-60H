def comparar_par_impar(num1, num2):
    if num1 % 2 == 0:
        print("O primeiro número é PAR")
    else:
        print("O primeiro número é ÍMPAR")

    if num2 % 2 == 0:
        print("O segundo número é PAR")
    else:
        print("O segundo número é ÍMPAR")


def multiplicar(a, b, c):
    resultado = a * b * c
    return resultado


def potencia(base, expoente):
    resultado = base ** expoente
    return resultado


def verificar_idade(idade):
    if idade == 18:
        print("Você tem 18 anos!")
    else:
        print("Você não tem 18 anos.")


def calcular_idade(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    return idade


def copa_1999():
    campeao = "Estados Unidos"

    if campeao == "Brasil":
        print("O Brasil ganhou a Copa de 1999!")
    else:
        print("O Brasil não ganhou a Copa de 1999.")


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
comparar_par_impar(n1, n2)


a = int(input("Digite o primeiro número para multiplicar: "))
b = int(input("Digite o segundo número para multiplicar: "))
c = int(input("Digite o terceiro número para multiplicar: "))
print("Resultado da multiplicação:", multiplicar(a, b, c))


base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
print("Resultado da potência:", potencia(base, expoente))


ano = int(input("Digite seu ano de nascimento: "))
idade = calcular_idade(ano)
print("Sua idade é:", idade)
verificar_idade(idade)


copa_1999()
       



