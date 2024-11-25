class Retangulo: 
    def __init__(self, lado_a, lado_b):
        self.lado_a= lado_a
        self.lado_b = lado_b
    def mudar_valores_lados(self, novo_a, novo_b):
        self.lado_a = novo_a
        self.aldo_b = novo_b
    def retornar_valor(self):
        return self.lado_a, self.lado_b
    
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso 
        self.altura = altura
    def envelhecer(self, anos):
        for _ in range (anos):
            if self.idade < 21:
                self.altura =+ 0.5
            self.idade +=1
    def engordar(self, quilos):
        self.peso += quilos
    def emagrecer(self, quilos):
        self.peso -+ quilos
    def crescer(self, centimetros):
        self.altura = centimetros /100
    def __str__(self):
        return(f"Nome: {self.nome}\nIdade: {self.idade} anos")