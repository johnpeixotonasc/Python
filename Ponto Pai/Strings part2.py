# Strings part2

a = "Diego"
b = "Mariano"

concatenar = a + " " + b +"\n" # irá cacatenar na mesma linha a variável a + b

print (concatenar) # irá imprimir a variável concatenar
print (concatenar.lower()) # irá imprimir a variável concatenar e deixar o texto minúsculo

print ("\n----------------------------*----------------------------\n")

print (concatenar.upper()) # irá imprimir a variável concatenar e deixar o texto maiúsculo

print (concatenar.strip()) # irá remover o caractere especial "\n"

print ("\n----------------------------*----------------------------\n")

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ") # irá listar a frase acima em e acrescenterá aspas
print (minha_lista)

minha_lista = minha_string.split("r") # irá listar a frase acima sempre que encontrar uma letra r
print (minha_lista)

print ("\n----------------------------*----------------------------\n")


busca = minha_string.find("rei") # irá verificar em qual posição se encontra a palavra rei
print (busca)

print(minha_string[busca:]) # irá imprimir a variável busca a partir da palavra rei

print ("\n----------------------------*----------------------------\n")

minha_string = minha_string.replace("rei", "rainha") # irá substituir a palavra rei pela palavra rainha
print (minha_string)