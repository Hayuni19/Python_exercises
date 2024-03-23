def média(x, y):
    '''
    Retorna a média de x e y.
    
    Args:
        x (float): O primeiro número.
        y (float): O segundo número.
        
    Returns:
        float: A média dos dois números.
    '''
    return (x + y) / 2

def negativos(lst):
    '''
    Exibe os números negativos contidos na lista lst, um por linha.
    
    Args:
        lst (list): A lista de números a serem verificados.
    '''
    for valor in lst:
        if valor < 0:
            print(valor)

# Verifique as docstrings usando a função help()
help(média)
help(negativos)
