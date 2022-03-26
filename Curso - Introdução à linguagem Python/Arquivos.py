# Arquivos

arquivo = open("arquivo.txt") # irá abrir o arquivo.txt

linhas = arquivo.readlines() # irá exibir as linhas do arquivo.txt
print (linhas)

for linhas in linhas: # irá exibir as linhas em forma de matriz
	print (linhas)


print ("-------------------------------------------*-------------------------------------------\n")

arquivo = open("arquivo.txt") # irá abrir o arquivo "arquivo.txt"
texto_completo = arquivo.read()

print (texto_completo)

print ("\n-------------------------------------------*-------------------------------------------\n")

w = open("arquivo2.txt", "w")

w.write("Esse é o meu arquivo")

w.close