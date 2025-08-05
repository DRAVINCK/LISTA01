#12. Um sistema recebe dados do usuário sempre em formato de texto (string). Para cálculos, é
#necessário converter os valores para números decimais.
#Pede-se
#• Crie um código que solicite dois valores decimais e exiba a média entre eles.
#• Explique teoricamente:
#1. Por que é necessário usar a função float() no input()?

valor1 = float(input("Digite o primeiro valor decimal: "))
valor2 = float(input("Digite o segundo valor decimal: "))

media = (valor1 + valor2) / 2

print(f"A média entre {valor1} e {valor2} é {media}")

#1 pra poder usar numeros quebrado que nao quebrar o codigo e tambem o input serve para ler a entrada do usuario