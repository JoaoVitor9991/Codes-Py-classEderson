from InquirerPy import inquirer

nome = inquirer.text("Qual é o seu nome? ").execute()
cor = inquirer.select("Qual é a sua cor? ", choices=["AZUL", "VERDE", "VERMELHO"]).execute()

def valida_email(vol):
    if "@" not in vol:
        raise ValueError("Por favor, insira um e-mail válido.")
    return vol 
email = inquirer.text("Qual é o seu e-mail", validate= valida_email).execute()

