valor = int(input("Digite o valor do saque (múltiplo de 10): "))

if valor % 10 != 0:
    print("Valor inválido. Digite um valor múltiplo de 10.")
else:
    print("Notas fornecidas:")
    for nota in [100, 50, 20, 10]:
        qtd, valor = divmod(valor, nota)
        if qtd:
            print(f"{qtd} nota(s) de R${nota}")
