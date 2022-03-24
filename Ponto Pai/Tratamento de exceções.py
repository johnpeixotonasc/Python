#		Tratamento de exceções

# exemplo divisão

a = 2
b = 0

try:	# significa tentar (tente fazer isso:)
	print(a/b)

except:	# exceção
	print ("Não é permitida a divisão por 0")

print ("O resultado do exponenciação a ao quadrado é: ", a**a)

""" O tratamento por exceções é muito usado para o programa não parar a excecução, como mostrado acima,o código
irá percorer a divisão por 0 que daria erro e printar na tela que não é permitida a divisão por 0"""