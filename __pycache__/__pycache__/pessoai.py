class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso 
        self.altura = altura
    def envelhecer(self, anos):
        for _ in range (anos):
            if self.idade < 21:
                self.altura += 0.5
            self.idade +=1
    def engordar(self, quilos):
        self.peso += quilos
    def emagrecer(self, quilos):
        self.peso -= quilos
    def crescer(self, centimetros):
        self.altura += centimetros /100
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade} anos\n"
            f"Peso: {self.peso:.2f} kg\n"
            f"Altura: {self.altura:.2f} m"
        )
pessoa = Pessoa("João", 18, 70, 1.70)


pessoa.envelhecer(5)


pessoa.engordar(3)


pessoa.emagrecer(2)


pessoa.crescer(5)


print(pessoa)