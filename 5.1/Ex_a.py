def meuIMC(peso, altura):
    imc=  peso /(altura ** 2)

    if(imc < 18.5):
        return 'Abaixo do peso'
    elif 18.5 <= imc <25:
        return 'Normal'
    else:
        return 'Sobrepeso'
    
print(meuIMC(86,1.90))
print (meuIMC(63,1.90))