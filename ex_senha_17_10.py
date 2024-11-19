while True:
    usuario = str(input("Digite o úsuario: "))
    senha = str(input("Digite a senha: "))
    if senha == usuario:
        print("Senha inválida. Tente novamente")
    else:
        print("Confirmado.")