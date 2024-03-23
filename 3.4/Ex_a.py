#Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string). 
#O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos. 
#Dependendo do resultado, uma mensagem apropriada deverá ser impressa. Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.


usuários = ['joe', 'sue', 'hani', 'sophie']

id = input('Login: ')

if id in usuários:

    print('Você entrou!')

else:

    print('Usuário desconhecido. ')

print('Fim.')
