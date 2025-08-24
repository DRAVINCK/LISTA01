quantidade_alunos = int(input("Digite a quantidade de alunos: "))
maior_nota = 0
menor_nota = 10
soma_notas = 0

for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma_notas += nota
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

media = soma_notas / quantidade_alunos

print(f"Media da turma: {media}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
