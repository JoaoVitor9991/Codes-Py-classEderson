class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    def aumenta_vol(self, aumentar, abaixar):
        self.aumenta_vol1 = aumentar 
        self.abaixar = abaixar 
    def mudar_canal(self, frente, tras):
        self.frente = frente
        self.tras = tras
    def mostrar_numero(self, ncanal):
        self.ncanal = ncanal 
        