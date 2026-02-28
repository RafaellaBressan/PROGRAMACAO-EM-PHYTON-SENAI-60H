def calcular():
    try:
        
        l = [1,2,3]
        n1  =  10
        n2  =  3
        x  = 100
        print(n1  / n2 + x)
        print(l[n2])
        
    except ValueError as erro:
        print(erro)
    except ZeroDivisionError as erro:
        print(erro)
    except TypeError as erro:
        print(erro)
    except NameError as erro:
        print(erro)
    except IndexError as erro :
        print(erro)
    else:
        print('Não existe erro...')
        
    finally:
        print('Fim de carregamento...')

# ZerroDivisionError
calcular()