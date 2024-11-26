class Encapsulamento():

        def __init__(self, num1, num2):
            self.__num1 = num1
            self.__num2 = num2

        def adicionar(self):
            return self.__num1+self.__num2
    
calc = Encapsulamento(20,10)
print(calc.adicionar())
