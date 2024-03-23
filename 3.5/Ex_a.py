#Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) 
#e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.

listaPalavras = eval(input('Digite a lista de palavras:'))

for palavra in listaPalavras:

  if len(palavra) == 4:

    print(palavra)

