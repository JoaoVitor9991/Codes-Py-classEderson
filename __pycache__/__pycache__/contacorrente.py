class ContaC:
    def __init__(self, numero_cont, nome_corrent, saldo= 0):
        self.numero_cont = numero_cont
        self.nome= nome_corrent
        self.saldo = saldo
    def alterar_nome(self, novo_nome):
        self.nome_corrent= novo_nome 
    def depositar(self, valor):
        if valor >0:
            self.saldo +=valor
        else:
            print("Valor de depósito inválido. ")
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
    def __str__(self):
        return (f"Numero de conta: {self.numero_cont}\n"
                f"Nome do correntista: {self.nome_corrent}\n"
                f"Saldo: {self.saldo:.2f}")
conta = ContaC(12345, "Joao")
print(conta) 
print()
                
               