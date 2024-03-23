# Python_exercises

 Pratique o conteúdo da semana fazendo os exercícios do livro Introdução a Computação Usando Python (Perkovic) que seguem abaixo:
 
Exercício 2.1
Escreva expressões algébricas Python correspondentes aos seguintes comandos:
(a) A soma dos 5 primeiros inteiros positivos.
(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
(c) O número de vezes que 73 cabe em 403.
(d) O resto de quando 403 é dividido por 73.
(e) 2 à 10ª potência.
(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
(g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
 
Exercício 2.2
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
(a) A soma de 2 e 2 é menor que 4.
(b) O valor de 7 // 3 é igual a 1 + 1.
(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
(d) A soma de 2, 4 e 6 é maior que 12.
(e) 1387 é divisível por 19.
(f) 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
 
Exercício 2.3
Escreva instruções Python que correspondem às ações a seguir e execute-as:
(a) Atribua o valor inteiro 3 à variável a.
(b) Atribua 4 à variável b.
(c) Atribua à variável c o valor da expressão a * a + b * b.
 
Exercício 2.4
Comece executando as instruções de atribuição:
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
(a) 'ant bat cod'
(b) ant ant ant ant ant ant ant ant ant ant'
(c) 'ant bat bat cod cod cod'
(d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
 
Exercício 2.5
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões usando a string s e o operador de indexação que é avaliado como:
(a) '0'
(b) '1'
(c) '6'
(d) '8'
(e) '9' 

Exercício 2.6
Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a primeiro e a última palavras em palavras, na ordem do dicionário.
 
Exercício 2.7
Dada a lista de notas de trabalho de casa dos alunos
>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
escreva:
(a) Uma expressão que avalia para o número de 7 notas.
(b) Uma instrução que muda a última nota para 4.
(c) Uma expressão que avalia para a nota mais alta.
(d) Uma instrução que classifica as notas da lista.
(e) Uma expressão que avalia para a média das notas.
 
Exercício 2.8
Em que ordem os operadores nas expressões a seguir são avaliados?
(a) 2 + 3 == 4 or a >= 5
(b) lst[1] * -3 < -10 == 0
(c) (lst[1] * -3 < -10) in [0, True]
(d) 2 * 3**2
(e) 4 / 2 in [1, 2, 3]
 
Exercício 2.9
Qual é o tipo do objeto ao qual essas expressões são avaliadas?
(a) False + False
(b) 2 * 3**2.0
(c) 4 // 2 + 4 % 2
(d) 2 + 3 == 4 or 5 >= 5
 
Exercício 2.10
Escreva expressões Python correspondentes ao seguinte:
(a) O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
(b) O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
(c) A área de um disco com raio a
(d) O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro ( a, b ) e raio r 

 
Exercício 3.1
Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula
celsius space equals 5 over 9 left parenthesis text  fahrenheit  end text minus 32 right parenthesis.
Seu programa deverá ser executado da seguinte forma:
>>>
Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0
 
Exercício 3.8
Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada e retorna a média dos números. Um exemplo de uso é:
>>> average(2, 3.5)
2.75
 
Exercício 3.9
Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado perímetro.py. Um exemplo de uso é:
>>> perimeter(1)
6.283185307179586
 
Exercício 3.10
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada.
>>> negatives([4, 0, −1, −3, 6, −9])
-1
-3
-9
 
Exercício 3.11
Acrescente a docstring retorna a média de x e y à função média() e a docstring exibe os números negativos contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando a ferramenta de documentação help(). Você deverá receber, por exemplo:
>>> help(média)
Ajuda sobre a função média no módulo __main__:
média(x, y)
retorna a média de x e y
 
Exercício 3.12
Desenhe um diagrama representando o estado dos nomes e objetos após esta execução:
>>> a = [5, 6, 7]
>>> b = a
>>> a = 3
 
Exercício 3.13
Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista original for:
>>> time = [’Ava’, ’Eleanor’, ’Clare’, ’Sarah’]
então a lista resultante deverá ser:
>>> time
[’Sarah’, ’Eleanor’, ’Clare’, ’Ava’]
 
Exercício 3.14
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
>>> ingredientes = [’farinha’, ’açúcar’, ’manteiga’, ’maçãs’]
>>> trocaPU(ingredientes)
>>> ingredientes
[’maçãs’, ’açúcar’, ’manteiga’, ’farinha’] 

Exercício 3.2
Traduza estas instruções condicionais em instruções if do Python:
(a) Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
(b) Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
(c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
(d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
 
Exercício 3.3
Traduza estas declarações em instruções if/else do Python:
(a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'
(b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.
 
Exercício 3.4
Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string). O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos. Dependendo do resultado, uma mensagem apropriada deverá ser impressa. Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar. Aqui está um exemplo de um login bem-sucedido:
>>>
Login: joe
Você entrou!
Fim.
E aqui está um que não tem sucesso:
>>>
Login: john
Usuário desconhecido.
Fim.
 
Exercício 5.1
Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa (em metros) e o peso (em quilos) e calcula o Índice de Massa Corporal (IMC) dessa pessoa. A fórmula do IMC é:
i m c space equals space fraction numerator p e s o over denominator a l t u r a squared end fraction.
Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5, 'Normal' se 18,5 <= imc < 25, e 'Sobrepeso' se imc >= 25.
>>> meuIMC(86, 1.90)
Normal
>>> meuIMC(63, 1.90)
Abaixo do peso

 
Exercício 3.5
Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.
>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote
 
Exercício 3.6
Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.
(a) Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
(b) Inteiros de 0 a 1 (isto é, 0, 1).
 
Exercício 3.7
Escreva um laço for que exiba a seguinte sequência de números, um por linha.
(a) Inteiros de 3 até 12, inclusive este.
(b) Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
(c) Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
(d) Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.
 
Exercício 4.1
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões (usando s e o operador de indexação) que sejam avaliadas como:
(a) '234'
(b) '78'
(c) '1234567'
(d) '0123'
(e) '789'
 
Exercício 4.2
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:
(a) A variável cont, a quantidade de ocorrências da string 'day' na string previsão.
(b) A variável clima, o índice em que a substring 'sunny' começa.
(c) A variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'.
 
Exercício 5.9
Escreva uma função soma2D() que aceita duas listas bidimensionais do mesmo tamanho (ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e incrementa cada entrada na primeira lista com o valor da entrada correspondente na segunda lista.
>>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
>>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
>>> soma2D(t,s)
>>> for linha in t:
      print(linha)
[4, 8, 4, 5]
[5, 2, 10, 3]
[8, 4, 6, 6] 


