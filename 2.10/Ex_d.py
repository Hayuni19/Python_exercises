#O valor da expressão Booleana que verifica se um ponto com coordenadas x e y 
#está dentro de um círculo com centro ( a, b ) e raio r 

import math

x = int(input("Insira o valor do x = "))
y = int(input("Insira o valor do y = "))
a = int(input("Insira o valor do centro_x = "))  # Coordenada x do centro da circunferência
b = int(input("Insira o valor do centro_y = "))  # Coordenada y do centro da circunferência
r = int(input("Insira o valor do raio = "))

dentro_do_circulo = (x - a)**2 + (y - b)**2 <= r**2

print("Verificação da circunferência:", dentro_do_circulo)



