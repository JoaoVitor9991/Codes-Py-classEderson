def cadastro():
    nome = input("Qual seu nome: ")
    idade = int(input("Idade: "))
    return nome, idade
print("Iniciando cadastro...")
nome,idade = cadastro()
print("Cadastro realizado com sucesso. ")
print("Seu nome é ", nome, "e voce tem ", idade, " anos de idade")