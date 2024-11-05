try:
    a = int(input("Digite uma palavra: "))
except ValueError:
    print("Digite apenas números")
except:
    print("Erro desconhecidos")
finally:
    print("Final do algoritmo")