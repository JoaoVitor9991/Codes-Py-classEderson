quantidade_produto = int(input("Digite a quantidade de produto"))
nome_produto = str(input("Digite o nome do produto: "))
valor_produto = float(input("Digite o valor unitário do produto: "))
desconto = (float(input("Digite o desconto a ser aplicado: ")))
valor_total = valor_produto * quantidade_produto 
valor_desconto = valor_total - (valor_total * desconto/100)

print(f"{nome_produto}")
print(f"{valor_total}")
print(f"{valor_desconto}")
