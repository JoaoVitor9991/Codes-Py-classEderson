while True:
    print("Digite qual operação deseja fazer \n 1- Soma\n 2- subtração\n 3- multiplicação\n 4- divisão\n ou 0 para encerar programa")
    op = int(input("Digite qual operação deseja fazer. "))

    if op == 0:
        print("Encerrando programa. ")
        break 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if op ==1:
        resultado = num1 + num2 
        print(f"Resultado da soma foi de: {resultado:.2f}")
    elif op ==2:
        resultado = num1 - num2
        print(f"Resultado da subtração foi de: {resultado:.2f}")
    elif op == 3:
        resultado = num1 * num2
        print(f"Resultado da multiplicação foi de: {resultado:.2f}")
    elif op == 4:
        resultado = num1 / num2
        print(f"Resultado da divisão foi de: {resultado:.2f}")
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado:.2f}")
        else:
            print("Erro! Divisão por zero não é permitido. ")
    else:
        print("Operação Inválida. Tente novamente")
 
