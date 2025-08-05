

valor = int(input("Digite o valor do saque (múltiplo de 10): "))

if valor % 10 != 0:
    print("Valor inválido. Digite um valor múltiplo de 10.")
else:
    cedulas_100 = valor // 100
    resto = valor % 100

    cedulas_50 = resto // 50
    resto = resto % 50

    cedulas_20 = resto // 20
    resto = resto % 20

    cedulas_10 = resto // 10

    print("Notas fornecidas:")
    if cedulas_100:
        print(f"{cedulas_100} nota(s) de R$100")
    if cedulas_50:
        print(f"{cedulas_50} nota(s) de R$50")
    if cedulas_20:
        print(f"{cedulas_20} nota(s) de R$20")
    if cedulas_10:
        print(f"{cedulas_10} nota(s) de R$10")
