n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
# for n1 in range (n2):
#     soma = n1 + n2
#     print(n1)
soma=0
for i in range(n1 +1, n2): 
    soma = soma + i
    print(i)

print(soma)