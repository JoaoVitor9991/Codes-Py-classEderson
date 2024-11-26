class Retangulo:
    def __init__(self, lado_a, lado_b):
        
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lados(self, novo_lado_a, novo_lado_b):
        
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_valor_lados(self):
        
        return self.lado_a, self.lado_b

    def calcular_area(self):
        
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        
        return 2 * (self.lado_a + self.lado_b)


def main():
    print("Bem-vindo ao programa de cálculo de retângulos!")
    lado_a = float(input("Informe o valor do lado A (comprimento): "))
    lado_b = float(input("Informe o valor do lado B (largura): "))
    
   
    retangulo = Retangulo(lado_a, lado_b)
    
    print("\n--- Resultados Iniciais ---")
    print(f"Área do retângulo: {retangulo.calcular_area()} m²")
    print(f"Perímetro do retângulo: {retangulo.calcular_perimetro()} m")
    
    
    tamanho_piso = float(input("\nInforme o tamanho de cada piso (em m²): "))
    quantidade_pisos = retangulo.calcular_area() / tamanho_piso
    print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
    
    rodape = retangulo.calcular_perimetro()
    print(f"Quantidade de rodapés necessários: {rodape:.2f} m")

    
    alterar = input("\nDeseja alterar os lados do retângulo? (s/n): ").lower()
    if alterar == 's':
        novo_lado_a = float(input("Informe o novo valor do lado A: "))
        novo_lado_b = float(input("Informe o novo valor do lado B: "))
        retangulo.mudar_valor_lados(novo_lado_a, novo_lado_b)
        print("\n--- Resultados Atualizados ---")
        print(f"Área do retângulo: {retangulo.calcular_area()} m²")
        print(f"Perímetro do retângulo: {retangulo.calcular_perimetro()} m")
    
if __name__ == "__main__":
    main()
