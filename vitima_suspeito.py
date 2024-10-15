p1 = str(input("Telefonou para a vítima? "))
p2 = str(input("Esteve no local do crime? "))
p3 = str(input("Mora perto da vítima? "))
p4 = str(input("Devia para a vítima? "))
p5 = str(input("Já trabalhou com a vítima? "))


cont=0
if p1.upper() == "SIM":
    cont=cont+1

if p2.upper() == "SIM":
    cont = cont + 1

if p3.upper() == "SIM":
    cont = cont +1

if p4.upper() == "SIM":
    cont = cont +1

if p5.upper() == "SIM":
    cont = cont + 1



if cont == 2:
    print("Classificação: Suspeita ")
elif cont >=3  and cont <=4:
    print("Classificação: Cúmplice")
elif cont == 5:
    print("ASSASSINO(A).")
elif cont <2:
    print("Inocente. ")