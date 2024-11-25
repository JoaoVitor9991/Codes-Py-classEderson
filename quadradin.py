class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho
    def mostrar_valor_lado(self):
        return self.tamanho_lado
    def calcular_area(self):
        return self.tamanho_lado **2
    
quadrado = Quadrado(5)
print(f"Tamanho do incial: {quadrado.mostrar_valor_lado()}")
print(f"Area inicial: {quadrado.calcular_area()}")

quadrado.mudar_valor_lado(5)
print(f"Novo tamanho do lado {quadrado.mostrar_valor_lado()}")
print(f"Nova area: {quadrado.calcular_area()}")