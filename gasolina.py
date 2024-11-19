gasolina_ou_alcool = str(input("G para gasolina ou A para Alcool ").upper())
litro = float(input("Qual a quantidade em litros? "))

if gasolina_ou_alcool == "A":
    preco_por_litro = 1.90
    if litro <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif gasolina_ou_alcool == "G":
    preco_por_litro = 2.50
    if litro <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    print("Tipo invalido! ")
    print("Desconto = 0")
    print("Valor = 0")

    valor_sem_desconto = litro * preco_por_litro
    