macas = int(input("Digite a quantidade maçãs que deseja comprar. "))
if macas >= 12:
    valor_macas = macas * 0.25
    print(f"Quantidade de maçãs foi de {macas} e o valor total foi de {valor_macas}")
elif macas <= 11:
    valor_macas = macas * 0.3
    print(f"Quantidade de maçãs foi de {macas} e o valor total foi de {valor_macas:.2f} ")
     