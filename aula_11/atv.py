import random


def soma1():
    print(10 + 10)


def soma2():
    n1 = int(input('digite o valor 1'))
    n2 = int(input('digite o valor 2'))
    soma  = n1 + n2
    print(soma)


def soma3(n1, n2):
    print(n1 + n2)


# otimização -  é a melhor utilização de uma função
def soma4(n1, n2):
    return n1  + n2 



n1 , n2  = 10,10
def soma5():
    print(n1 + n2)


soma1()
soma2()
soma3(10,10)
print(soma4(10,10))
soma5()




soma = soma4()  




