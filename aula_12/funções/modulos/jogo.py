import random 

def advinha(chute):
    n =  random.randint(1,10)
    if n == chute:
        return 'ganhou', n
    else:
        return 'perdeu', n