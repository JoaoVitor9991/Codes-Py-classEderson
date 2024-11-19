sal_atual = float(input("Digite o seu salário atual: "))

if sal_atual <= 280:
    por=20
elif sal_atual > 280 and sal_atual <= 700:
    por=15
elif sal_atual > 700 and sal_atual <= 1500:
    por=10
elif sal_atual > 1500:
    por=5

aumento_Sal = sal_atual * por/100 
sal_com_aumento = sal_atual + aumento_Sal
print(f"Salário atual é :{sal_atual:.2f}")
print(f"Com o aumento de {por}% será de: {sal_com_aumento}")
print(f"Salário anterior: {sal_atual}")
