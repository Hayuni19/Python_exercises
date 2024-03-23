#O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados 
#têm comprimentos a e b

import math


a = float(input("Insira o valor de A = "))
b = float(input("Insira o valor de B = "))

hip = math.sqrt(a**2 + b**2)

print("A hiportenusa é = ",hip)