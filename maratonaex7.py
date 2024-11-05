while True:
    login = (input("Digite o login: "))
    senha = (input("Digite a senha: "))

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False


    if len(senha) >= 8:
        for caracter in senha:
            if caracter.isupper():
                tem_maiuscula:True
            elif caracter.islower():
                tem_minuscula: True
            elif caracter.isdigit():
                tem_numero: True
    

        if tem_maiuscula and tem_minuscula and tem_numero:
            print("Login válido. ")
            
        else:
            print("Login Inválido. ")
    else:
            print("Login Inválido. ")
  



