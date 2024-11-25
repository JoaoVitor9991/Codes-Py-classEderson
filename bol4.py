class Bola:
    def __init__(self, cor, circuferencia,material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material 
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    def mostra_cor(self):
        return self.cor
    
bola = Bola ("Vermelha", 30, "couro")
    