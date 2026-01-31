print('SISTEMA DE NOTAS')
print('...' * 10)
nome_aluno = input('Nome do aluno: ')
print()
n1_port = float(input('Nota Portugues: '))
n2_mat = float(input('Nota Matemática: '))
n3_ing =float(input('Nota ingles: '))
print()
media = (n1_port + n2_mat + n3_ing)/3
print('SITUAÇÃO DO ALUNO: ')
print('...' * 10)
print()
aprovado = media > 7
reprovado = media < 5
recuperacao = media >=5 and media < 7
print('Aprovado? - ', aprovado)
print('Reprovado? - ', reprovado)
print('Recuperação? - ', recuperacao)
