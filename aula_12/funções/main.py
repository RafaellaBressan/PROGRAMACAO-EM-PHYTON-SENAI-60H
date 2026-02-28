
import modulos.calculos_estatisticos as cl
from modulos.jogo import advinha
import modulos.visualizacao
from modulos import *


def main():
    f =  [1,2,3,5,5,6]
    moda_1  = cl.moda(f)
    print(moda_1)


    mediana_1 =  cl.mediana(f) 
    print(mediana_1)


    media_1 =  cl.media(f)
    print(media_1)


    print('****' * 15)



    t =  int(input('Número: '))
    resultado = advinha(t)
    print(resultado)



    print('****' * 15)



    mostrar_1 =  modulos.visualizacao.imagem1()
    print(mostrar_1)
    mostrar_2 =  modulos.visualizacao.imagem1()
    print(mostrar_2)
    mostrar_3 =  modulos.visualizacao.visualizar('text')
    print(mostrar_3)


main()