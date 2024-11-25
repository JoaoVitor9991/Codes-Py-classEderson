class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    def alterar(self, alterar_nome, alterar_fome, alterar_saude, alterar_idade):
        self.alterar_nome = alterar_nome
        self.alterar_fome = alterar_fome
        self.alterar_saude = alterar_saude
        self.alterar_idade = alterar_idade
    def humor(self, alegre, triste, normal):
        self.alegre = alegre
        self.normal = normal
        self.triste = triste
    def saude(self, Ndoente, Doente):
        self.Ndoente= Ndoente
        self.Doente = Doente
        