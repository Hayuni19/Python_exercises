#Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula
#celsius space equals 5 over 9 left parenthesis text  fahrenheit  end text minus 32 right parenthesis.
#Seu programa deverá ser executado da seguinte forma:

f = int(input("Digite a temperatura em graus Fahrenheit: "))

cel = ((5/9)*(f-32))

print("A temperatura em graus Celsius é = ", cel)