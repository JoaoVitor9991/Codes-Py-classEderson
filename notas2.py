n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a primeira nota: "))
n4 = float(input("Digite a segunda nota: "))
m = (n1 + n2 + n3 + n4) / 4

if m >= 9.1 and m <= 10:
    print(f"APROVADO! Sua nota foi de {m} e o conceito A")
elif m >= 7.5 and m <=9:
    print(f"APROVADO! Conceito B. E sua nota foi de: {m}")
elif m >= 6.0 and m < 7.5:
    print(f"APROVADO! Conceito C. E sua nota foi de: {m}")
elif m >= 4.1 and m <=5.9:
    print(f"REPROVADO! Conceito D. E sua nota foi de: {m}")
elif m >= 0 and m <= 4.0:
    print(f"REPROVADO! Conceito E. Sua nota foi de: {m}")