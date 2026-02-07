# e-commerce 
# lista de produtos
# lista de valores 
# poder comprar um produto


print('E-COMMERCE')
lista_prod = ['','hd', 'pen-drive','fone', 'carregador']
lista_valores = [0,450.0, 100.0,350.0,90.0]
carrinho = []
meu_valor = []
print('***' * 20)
print(f'''
PRODUTOS:
ID            PRODUTOS       VALOR R$
{lista_prod.index('hd')}                 {lista_prod[1]}        {lista_valores[1]}
{lista_prod.index('pen-drive')}          {lista_prod[2]}        {lista_valores[2]}         
{lista_prod.index('fone')}               {lista_prod[3]}        {lista_valores[3]}
{lista_prod.index('carregador')}         {lista_prod[4]}        {lista_valores[4]}


''')
print('***' * 20)



produto1 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto1])
meu_valor.append(lista_valores[produto1])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )


produto2 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto2])
meu_valor.append(lista_valores[produto2])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )


produto3 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto3])
meu_valor.append(lista_valores[produto3])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )


formas_pagamentos =  ['pix','cc','cd']
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('Digite a forma de pagamento: ')
indice = formas_pagamentos.index(escolhe_forma)
print('Forma de pagamento: ', formas_pagamentos[indice])
print('Obrigada volte sempre! ')


