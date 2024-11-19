produtos = {
    1: ("Camistas ", 38.00),
    2: ("Short", 35.00 ),
    3: ("Meia ", 10,00),
    4: ("Cueca", 15,00),
    5: ("Casaco", 75,00)

}
produto_id = int(input("Selecione o número do produto: "))
if produto_id not in produtos:
    print("Produto invalido")
else:
    produto_nome, preco = produtos[produto_id]
    dinheiro = float(input("Insira o valor a pagar: "))
    if dinheiro < preco:
        print("Valor insuficiente")
    else:
        troco = dinheiro - preco
        print("Compra realizada")
        print("Troco de: ", troco)