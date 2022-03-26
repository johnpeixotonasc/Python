# Listas parte 1

# Os valores entre [] serão armazenados dentro das variáveis
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4]
minha_lista3 = ["abacaxi", 2, 9.89, True]

print (minha_lista) # irá imprimir a variável minha_lista
print (minha_lista2) # irá imprimir a variável minha_lista2
print (minha_lista3) # irá imprimir a variável minha_lista3
print (minha_lista[2]) # irá imprimir o indíce 2 da variável minha_lista

for item in minha_lista: # irá imprimir os valores da variável minha_lista um abaixo do outro
	print (item)

print ("\n------------------------------------*------------------------------------\n")

#		Verificando o tamanho da minha_lista")

tamanho = len(minha_lista) # irá verificar o tamanho da variável minha_lista

print(tamanho)

print ("\n------------------------------------*------------------------------------\n")

#		Adicionando elementos

minha_lista.append("limão")

print(minha_lista)

print ("\n------------------------------------*------------------------------------\n")

#		Verificando se um ítem pertence a minha lista

if 3 in minha_lista2:
	print("3 está na lista")

print ("\n------------------------------------*------------------------------------\n")

# 		Removendo elementos da minha lista

del minha_lista[2:]
print (minha_lista)