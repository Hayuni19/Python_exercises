#Escreva uma função soma2D() que aceita duas listas bidimensionais do mesmo tamanho (ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e incrementa cada entrada na primeira lista com o valor da entrada correspondente na segunda lista.
#>>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
#>>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
#>>> soma2D(t,s)
#>>> for linha in t:
#      print(linha)
#[4, 8, 4, 5]
#[5, 2, 10, 3]
#[8, 4, 6, 6] 

def soma2D(lista1, lista2):
    
    if len(lista1) != len(lista2) or len(lista1[0]) != len(lista2[0]):
        print("As listas não têm o mesmo tamanho.")
        return
    

    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            lista1[i][j] += lista2[i][j]

t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]

soma2D(t, s)

for linha in t:
    print(linha)


# Verifica se as listas têm o mesmo número de linhas e colunas
    # Itera sobre as linhas e colunas e incrementa os valores