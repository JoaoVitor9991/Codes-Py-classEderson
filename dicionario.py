tradutor1 = {}
tradutor1 = {"pineapple" : "abacaxi", "apple" : "maça", "orange" : "laranja"}
print(tradutor1)
del(tradutor1)["apple"]
print(tradutor1.pop("banana", "fruta nao encontrada"))
#clear para limpar 
tradutor1.clear()
print(tradutor1)
print("laranja" in tradutor1.values())
print(tradutor1.values())