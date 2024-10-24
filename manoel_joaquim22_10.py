while True:
    total_compra = 0
    cliente = int(input("1 - cliente \n 0-sair "))
    if cliente == 1:
        while True: 
            preco = float(input("Digite o preço do produto ou digite 0 para finalizar a compra: "))
            if preco == 0:
                break    
            nome_produto = str(input("Digite o nome do produto: "))
            total_compra += preco
            print(f"{nome_produto}: {preco}")
        print(f"total: {total_compra}") 

        while True:
            pagamento = float(input("Digite o valor que você pagará? "))
            if pagamento < total_compra:
                print("Valor insuficiente. Tente novamente. ")
                
            else:
                troco = pagamento - total_compra
                print("troco de: ", troco)
                break
    elif cliente==0:
        break





        