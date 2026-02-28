print("Exercício 1 - Número Inteiro")

try:
    numero = int(input("Digite um número inteiro: "))
    print("Você digitou o número:", numero)
except ValueError:
    print("Erro! Você precisa digitar um número inteiro.")

print("\n-------------------------\n")


print("Exercício 2 - Divisão")

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 / numero2
    print("Resultado da divisão:", resultado)

except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.")
except ValueError:
    print("Erro! Digite apenas números.")

print("\n-------------------------\n")

print("Exercício 3 - Índice da Lista")

lista = ["maçã", "banana", "laranja", "uva"]

try:
    indice = int(input("Digite o índice que você quer acessar (0 a 3): "))
    print("Elemento escolhido:", lista[indice])

except IndexError:
    print("Erro! Índice inválido.")
except ValueError:
    print("Erro! Digite um número inteiro.")