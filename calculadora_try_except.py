resultado = 0
def calculadora():
    print("Selecione a operação ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    try: 
        ope = int(input("Digite a operação..."))
    except:
        print("valor inválido")
        # if ope not in  (1, 2, 3, 4):
        #     raise ValueError("Operação Invalida. ")
    else:   
        try:
            num1 = int(input("Digite um número. "))
            num2 = float(input("Digite outro número:"))
        except:
            print("valor inválido")
            
        if ope == 1:
            resultado == num1 + num2
            print(f"O resultado foi de {resultado}")
        elif ope == 2:
            resultado == num1 - num2 
        elif ope == 3:
            resultado == num1 * num2
        elif ope == 4:
            try: 
                resultado = num1 / num2 
                print(f"Resultado da divisão foi de: {resultado:.2f}")
            except ZeroDivisionError:
                print("Erro! Divisão por zero não é permitida.")
            except ValueError:
                print("Valor Inválido. Digie um número Válido. ")
            except ValueError as ve:
                print(ve)
                print("Operação Invalida. Tente novamente")

calculadora()
    

        
    