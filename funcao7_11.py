def par(x):
    if (x)>0:
        return "P"
    elif x<0:
        return "N"
    else:
        return "O valor é zero. "
    
while True:
    num = int(input("Digite para positivo ou  para negativo: "))
    if par (num)== "N":
        print("Negativo")
    elif par (num)=="P":
        print("Positivo")
    else:
        print(par(num))    
    