#Verificador de Palíndromos
#o Peça uma palavra ou frase.
#o Verifique se é um palíndromo (lê-se igual de frente para trás).


frase = input("Digite uma palavra ou frase: ").replace(" ", "").lower()

if frase == frase[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
