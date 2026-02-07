

# ESTRUTURDA DE DADOS


v = 10 # 1 dado (VARIAVEIS)
lista = [1,2,3] # list varios dados (LISTAS)
tuplas = (1,2,3) # tuple varios dados imutaveis (TUPLAS)
conjunto = {1,2,3} # set varios dados numeros s/ repetição (CONJUNTOS)
dicionario = {'key': 'value'} # dict detalhada (DICIONARIOS)






usuario = {
    'nome' : 'Paulo', 
    'idade':25, 
    'endereço': 'rua 10', 
    'curso': ('python','js', 'go'),
    'documento':{132132132,1231231321,2123231231,123132132},
    'livros':{
     'taleb':['antifragil','cisne negro'],
     'harari':['homodeus']


    }
    }



estoque = {
'eletronicos':{
'iphone':['17', '15','14'],
'tvs':['samsumg','lg' ],
},
'moveis':{
'mesas':['etna','x'],
'cadeiras':['etan','leroy']
}
}



d =  dict(a = 10, b = 20, c = 30)
print(d)




tupla = (1,2,3)
tuplas = 1,2,3
t = tuple(range(1,11))


tupla+=(t,tuplas)


print(tupla)


# sum(t)
# len(t)
# max()
# print(dir(t))



# -------------------------------------



# conjunto 




conjunto = {10,20,30,40,40}
c = set(range(1,11))
print(conjunto)


c1 =  {1,2,3}
c2 = {1,2,4,5,6}
c1.add(100)


print(c1)

