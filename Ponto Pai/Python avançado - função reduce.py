# Python avançado: função reduce

from functools import reduce # from chama a função functools e import irá importar a tabela reduce
"""functools — Funções e operações de ordem superior em objetos chamáveis. 
O módulo functools é para funções de ordem superior: funções que atuam ou
retornam outras funções. Em geral, qualquer objeto chamável pode ser tratado
como uma função para os propósitos deste módulo."""


def soma(x, y):
    return x + y

lista = [1, 3, 5, 10, 20]

# Quero obter todos os valores dentro dessa lista

soma = reduce(soma, lista) # Para cada elemento da variável lista ele irá somar e pegar x como o primeiro valor e y a soma de todos os valores e no final somar
print ("O resultado da soma é: ", soma) 