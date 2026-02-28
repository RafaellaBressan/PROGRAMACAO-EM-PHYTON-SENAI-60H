import estatistica

notas = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

print("\n===== RESULTADOS =====")

print("Média:", estatistica.calcular_media(notas))
print("Moda:", estatistica.calcular_moda(notas))
print("Desvio Padrão:", estatistica.calcular_desvio_padrao(notas))
print("Maior Nota:", estatistica.maior_nota(notas))
print("Menor Nota:", estatistica.menor_nota(notas))