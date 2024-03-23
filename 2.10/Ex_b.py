#O valor da expressão que avalia se o comprimento da hipotenusa acima é 5

import math


a = float(input("Insira o valor de A = "))
b = float(input("Insira o valor de B = "))

hip = math.sqrt(a**2 + b**2) == 5

print("A hiportenusa é = ",hip) #retorna um bool
