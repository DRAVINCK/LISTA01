qtd = int(input("Quantidade de alunos: "))
notas = [float(input(f"Nota do aluno {i+1}: ")) for i in range(qtd)]

print(f"Média: {sum(notas)/qtd}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
