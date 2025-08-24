#IMC – Índice de Massa Corporal
#o Solicite peso e altura do usuário.
#o Calcule o IMC e classifique como “Abaixo do peso”, “Normal”, “Sobrepeso” ou “Obeso”.


peso = float(input("qual o seu peso em kg: "))
altura_cm = float(input("qual a sua altura em cm: "))

altura = altura_cm / 100

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo do peso")
elif 18.5 <= IMC <= 24.9:
    print("Peso normal")
elif 25 <= IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

