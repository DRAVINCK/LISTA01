#Cálculo de Média e Aprovação
#o Peça o nome e duas notas de um aluno.
#o Calcule a média e informe se foi aprovado (nota ≥ 6).

nome = input("Qual o seu nome?  ")

nota1 = input("qual a sua primeira nota? ")

nota2 = input("qual a sua segunda nota? ")

media = (int(nota1) + int(nota2)) / 2


if media >= 6:
    print(f"{nome}, sua media: {media} - Aprovado!")
else: print(f"{nome}, sua media: {media} - Reprovado!")
