print('Seja bem-vindo ao e-commerce bom e barato!')
print('Promoções disponíveis:fone bluetooth por apenas 190 reais, corre que dá tempo!')

ecommerce = {
'livro':25.10,
'tablet':800.0,
'fone':190.0,
'celular':1000.99
}


carrinho = {
'produtos':[],
'valores':[]
}


produto1 = input('produto: ')
produto2 = input('produto: ')


carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])


soma =  sum(carrinho['valores'])

print('Total -  R$', soma)

print(carrinho)

