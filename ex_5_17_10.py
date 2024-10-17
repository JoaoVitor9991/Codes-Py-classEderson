while True:
    n = str(input("Digite seu nome: "))
    if len(n) < 3:
        print("Nome Inválido. Tente novamente.")
    else:
        print("Nome válido")
        break
while True:    
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade <= 150:
        print("Idade válida. ")
        break
    else:
        print("Idade inválida. ")
        
while True:
    sal = float(input("Digite seu salário: "))
    if sal <=0:
        print("Salário Inválido. Tente novamente. ")
    else:
        print("Sálario válido. ")
        break
while True:    
    sexo = str(input("Digite o sexo F, M ou O: ").upper())
    if sexo == "f" or sexo == "m" or sexo == "o":
        print("Sexo válido.")
        break
    else:
        print("Sexo Inválido. Tente novamente")
        

while True:
    civil = str(input("Digite seu estado Civil: S, C, V ou D").upper())
    if civil == "S" or civil == "C" or civil == "V" or civil == "D":
        print("Estado civil válido. ")
        break
    else:
        print("Estado civil inválido. Tente novamente")
        

    

    
   

