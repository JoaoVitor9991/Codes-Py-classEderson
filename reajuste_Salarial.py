sal_atual = float(input("Digite o seu salário atual: "))


if sal_atual <= 280:
    aumento_Sal = sal_atual * 0.2
    sal_com_aumento = sal_atual + aumento_Sal
    print(f"Salário atual é :{sal_atual:.2f}")
    print(f"Com o aumento de 20% será de: {sal_com_aumento}")
elif sal_atual > 280 and sal_atual <= 700:
    aumento_Sal = sal_atual * 0.15
    sal_com_aumento = sal_atual + aumento_Sal
    print(f"Salário atual é :{sal_atual:.2f}")
    print(f"Com o aumento de 15% será de: {sal_com_aumento}")
elif sal_atual > 700 and sal_atual <= 1500:
    aumento_Sal = sal_atual * 0.10
    sal_com_aumento = sal_atual + aumento_Sal
    print(f"Salário atual é :{sal_atual:.2f}")
    print(f"Com o aumento de 10% será de: {sal_com_aumento}")
elif sal_atual > 1500:
    aumento_Sal = sal_atual * 0.05 
    sal_com_aumento = sal_atual + aumento_Sal
    print(f"Salário atual é :{sal_atual:.2f}")
    print(f"Com o aumento de 5% será de: {sal_com_aumento}")
