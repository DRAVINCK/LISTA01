#Calculadora Simples
#o Peça dois números e exiba a soma, subtração, multiplicação e divisão.
#o Utilize condicionais para verificar divisão por zero.

num1 = int(input("primeiro num: "))
num2 = int(input("segundo num: "))

print(f"soma: {num1 + num2}")
print(f"sub: {num1 - num2}")
print(f"mult: {num1 * num2}")

if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:
    print("Divisão: Erro! Não é possível dividir por zero.")
