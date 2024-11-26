class Retangulo: 
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valores_lados(self, novo_a, novo_b):
        """Altera os valores dos lados do retângulo"""
        self.lado_a = novo_a
        self.lado_b = novo_b

    def retornar_valores_lados(self):
        """Retorna os valores atuais dos lados"""
        return self.lado_a, self.lado_b

    def calcular_area(self):
        """Calcula a área do retângulo"""
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        """Calcula o perímetro do retângulo"""
        return 2 * (self.lado_a + self.lado_b)


def main():
    print("Bem-vindo ao programa de cálculo de Retângulos!\n")
    
    
    lado_a = float(input("Informe o valor do Lado A (comprimento): "))
    lado_b = float(input("Informe o valor do Lado B (largura): "))
    
   
    retangulo = Retangulo(lado_a, lado_b)
    
    #
    print("\n--- Resultados Iniciais ---")
    print(f"Área: {retangulo.calcular_area()} m²")
    print(f"Perímetro: {retangulo.calcular_perimetro()} m")
  
    tamanho_piso = float(input("\nInforme o tamanho de cada piso (em m²): "))
    quantidade_pisos = retangulo.calcular_area() / tamanho_piso
    print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
    
    rodape = retangulo.calcular_perimetro()
    print(f"Quantidade de rodapés necessários: {rodape:.2f} m")
    
    
    alterar = input("\nDeseja alterar os lados do retângulo? (s/n): ").lower()
    if alterar == 's':
        novo_a = float(input("Informe o novo valor do Lado A: "))
        novo_b = float(input("Informe o novo valor do Lado B: "))
        retangulo.mudar_valores_lados(novo_a, novo_b)
        
        
        print("\n--- Resultados Atualizados ---")
        print(f"Área: {retangulo.calcular_area()} m²")
        print(f"Perímetro: {retangulo.calcular_perimetro()} m")
    
if __name__ == "__main__":
    main()
