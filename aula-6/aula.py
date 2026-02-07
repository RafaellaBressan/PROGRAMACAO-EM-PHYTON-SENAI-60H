# a = 0
# b = 1
# c = 2
# d = 3


nomes = []


nome1 = 'aluno1'
nome2 = 'aluno2'


nomes.append(aluno1)
nomes.append(aluno2)


print(nomes)
l = [1,1,3,5]
a,b,c,d = l


print(a,b,c,d)


# criar uma lista com valores declarativos
# l = list(range(1,201,9))

variavel  =  10
varivel2 = 'text'
variavel3 =  True
variavel4 =  5.2

lista  =  [1,2,3,4]

#acessando indices
print(lista[2])

print(lista[0] + lista[2])

# alteração do valor de algum indice
lista[3] = 100

print(lista)

print(lista[1]**2)

# alterar / verificar dado da lista
# alterar -  inserir dados

# verifica os métodos que posso utilizar
# print(dir(lista))

# append() -  Adiciona no final da lista
lista.append(100) 

print('lista - ', lista)
# insert() - add a partir do indice 
lista.insert(1,'test')
print(lista)

# extend() -  add no final quantos você quiser
lista.extend([1,2,3,4,5])
print(lista)

# +=  add no final quantos você quiser
lista+=(1,2,3,5)
print(lista)


# ------------------------------------


# removo dados da lista

# remove -  remove a partir do valor

lista.remove('test')
print(lista)

# pop -  ultimo
lista.pop()

# pop(indice) -  remove o indice

lista.pop(0)
print(lista)

# del - remover a partir do indice
del lista[1]
print(lista)
# ------------------------------------------

# metodos e funções que verificam algum dado da lista
# ações
# menor valor
print(min(lista))
# maior valor
print(max(lista))
# comprimento da lista
print('tamanho', len(lista))
# quantos itens do valor declarado
print(lista.count(3))


l = [1,2,3]
print(len(l))


# ordenar a lista /  revertendo a ardem
lista.reverse()

print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


# sum  -  somar todos os dados
print(sum(lista))

# copy -  copiar
x  = lista.copy()
print(x)

# clear -  limpa
# lista.clear()
# print(lista)

# index -  verifica a posição do indice
indice =  lista.index(100)
print(indice)