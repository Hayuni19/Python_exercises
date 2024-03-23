#Supondo que a variável previsão tenha recebido a string
#'It will be a sunny day today'
#escreva instruções Python correspondentes a estas atribuições:
#Saída:  A variável clima, o índice em que a substring 'sunny' começa.

previsao = 'It will be a sunny day today'

clima = previsao.find('sunny')

print(clima) # vai aparecer 13, pois é o índice que começa a string