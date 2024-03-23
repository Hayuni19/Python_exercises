import math

def perimeter(radius):
    '''
    Calcula o perímetro de um círculo com base no raio fornecido.

    Args:
        radius (float): O raio do círculo (deve ser um número não negativo).

    Returns:
        float: O perímetro do círculo.
    '''
    if radius < 0:
        raise ValueError("O raio não pode ser negativo.")
    
    return 2 * math.pi * radius
