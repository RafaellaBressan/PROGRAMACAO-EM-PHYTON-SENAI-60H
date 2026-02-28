import statistics


def calcular_media(notas):
    return statistics.mean(notas)


def calcular_moda(notas):
    return statistics.mode(notas)


def calcular_desvio_padrao(notas):
    return statistics.pstdev(notas)


def maior_nota(notas):
    return max(notas)


def menor_nota(notas):
    return min(notas)