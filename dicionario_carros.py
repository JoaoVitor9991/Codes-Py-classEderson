dados = {
    "Crossfox" : {"Km" : 3500, "ano":
     2005}, "DS5": {"Km": 17000, "ano" :2015},
     "Fusca": {"Km" : 130000, "ano": 1979},
     "Jetta": {"Km": 56000, "ano" : 2011},
     "Passat": {"Km": 62000, "ano" : 1999}
}

print(dados)
print(dados.get("Gol", "Veiculo não encontrado. "))