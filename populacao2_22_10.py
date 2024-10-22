while True :
        
    populacao_a = int(input("Digite o número da primeira população: "))
    populacao_b = int(input("Digite o número da segunda população: "))
    taxa_a = float(input("Digite o número da taxa de cresimento da primeira população: "))
    taxa_b = float(input("Digite o número da taxa de crescimento da segunda população: "))
    anos = 0
    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_a / 100
        populacao_b += populacao_b * taxa_b / 100 
        anos += 1
        print (anos)
    print(f"Serão necessários {anos} anos para população A passar a população B. ")
    b = str(input("Você quer encerrar o programa? (S/N)").upper())
    if b == "S":
        break
        
