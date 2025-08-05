#11. Um professor decidiu que a nota mínima para aprovação será 6.0. Porém, se o aluno tiver frequência
#inferior a 75%, ele será reprovado, mesmo que a nota seja maior que 6.
#Pede-se
#• Desenvolva um código em Python que leia a nota e a frequência (%) do aluno e exiba se ele foi
#aprovado ou reprovado.
#• Explique teoricamente:
#1. Por que o uso do operador lógico and é necessário nessa situação?
#2. O que aconteceria se fosse usado or no lugar de and?

nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno (%): "))

if nota >= 6.0 and frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")


#1 o and usa para verificar as duas condicoes se é maior que 6 e menor que 75
#2 seria verificado um ou outro, no caso se maior que 6 ou menor igual a 75

