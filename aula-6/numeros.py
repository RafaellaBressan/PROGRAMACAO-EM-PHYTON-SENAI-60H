range
dados = []

print (dados)
lista = [5,6,7,8]

lista.append(9)

print (lista)

lista.remove(5)

print (lista)

carros = ['sportage','kicks','uno']
print(carros, lista)

carros+=(dados)
print(carros)

formas_pagamentos =  ['pix','cc','cd']
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('Digite a forma de pagamento: ')
indice = formas_pagamentos.index(escolhe_forma)
print('Forma de pagamento: ', formas_pagamentos[indice])
print('Pagamento efetuado!')