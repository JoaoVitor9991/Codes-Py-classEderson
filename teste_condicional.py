x = 100
if x > 0: 
    print("X é maior que 0")
print("Término.")
print("----------------------------------------------------------------------------")
idade = 18
if idade < 20:
   print("Você é jovem")
print("----------------------------------------------------------------------------")

age = int(input("Digite sua idade: "))
if age == 16:
    print("Pode Votar. ")
else:
    if age >= 18:
        print("Pode dirigir.")
    else:
        if age < 16:
            print("Apenas estude.")
