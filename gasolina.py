gasolina_ou_alcool = str(input("G para gasolina ou A para Alcool "))
litro = float(input("Qual a quantidade em litros? "))

if gasolina_ou_alcool.upper() == "G":
    if litro <= 20:
        valor = litro * 0.04
        print(valor)
    elif litro > 20:
        valor = litro * 0.06
        print(valor)
    