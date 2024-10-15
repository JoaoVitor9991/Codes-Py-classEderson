n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

m = (n1 + n2 + n3 + n4) / 4

if m == 10:
    print(f"{m} Aprovado com Distinção!! ")

elif m >= 7:
    print(f"{m} Aprovado! ")
elif m <7:
    print(f"{m} Reprovado. ")
 
