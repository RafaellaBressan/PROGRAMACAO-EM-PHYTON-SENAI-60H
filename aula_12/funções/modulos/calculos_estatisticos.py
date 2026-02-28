import statistics


f  =  [1,2,3,6,5,5,7]
def moda(frequencia):
    # moda é o que mais aparece 
    moda =  statistics.mode(frequencia)
    return moda


f  =  [1,2,3,6,5,5,7]
f.sort()
# print(f)

def mediana(f):
    mediana =  statistics.median(f)
    return mediana


# x  =  [10,10,10,12,15]
def media(f):
    media =  statistics.mean(f)
    return media
    


