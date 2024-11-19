a = 0 
b = 1
n = int(input("Digite o número: "))

for i in range(n):
    print(a, end=" ")
    temp = a 
    a = b
    b = temp + b