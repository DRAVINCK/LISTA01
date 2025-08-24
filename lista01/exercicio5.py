#Classificação de Idade
#o Peça a idade do usuário.
#o Classifique como “Criança” (0-12), “Adolescente” (13-17), “Adulto” (18-59) ou “Idoso”
#(60+).


idade = int(input("Insira sua idade: "))

if 0 < idade <= 12:
    print("Criança")
elif 13 <= idade < 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")