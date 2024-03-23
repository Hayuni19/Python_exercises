#(a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; 
#caso contrário, exiba 'Definitivamente não é um ano bissexto.'

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')
