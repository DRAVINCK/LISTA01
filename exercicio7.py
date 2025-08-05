
numero = int(input("Digite o número para a tabuada: "))
limite = int(input("Digite até qual número você deseja a tabuada: "))


for i in range(1, limite + 1):
    print(f"{numero} x {i} = {numero * i}")
