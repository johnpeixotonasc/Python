# Números aleatórios

import random # irá importar o módulo random (números aleatórios)


random.seed(1) # irá escolher um número aleatório entre 0 e 10 repetidamente
numero = random.randint(0, 10) # irá buscar um número aleatório entre 0 e 10 e armazenará na variável numero
print (numero)

#		Escolhendo um núro aleatório dentro de uma lista

lista = [6, 45, 9] # defini os valores 6, 45 e 9 para a variável lista
numero1 = random.choice(lista) # a variável numero1 irá escolher um número dentro da variável lista
print (numero1)