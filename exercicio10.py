#Simulação de Compras
#o Peça nome e preço de 3 produtos.
#o Calcule o total, aplique desconto de 10% se o valor ultrapassar R$ 100 e mostre o valor final.

nome1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input(f"Digite o preço do {nome1}: "))

nome2 = input("Digite o nome do segundo produto: ")
preco2 = float(input(f"Digite o preço do {nome2}: "))

nome3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input(f"Digite o preço do {nome3}: "))

total = preco1 + preco2 + preco3

if total > 100:
    total *= 0.9

print(f"Total final: R$ {total:.2f}")
