# Python avançado: função enumerate

lista = ["abacate", "bola", "cachorro"]

print ("\n------------------------------------*------------------------------------\n")

print("\nDe maneira simples:\n")
for i in lista:
    print (i)

print ("\n------------------------------------*------------------------------------\n")

print("\nPara pegar o indice:\n")

for i in range(len(lista)): # função range para criar um vetor e o len para verificar o tamanho da lista
    print (i, lista[i])

print ("\n------------------------------------*------------------------------------\n")

print ("\nUtilizando a função enumerate:\n")

for i, nome in enumerate(lista): # Enumerate irá retornar um valor i que é o indice e o valor de um nome do item
    print (i, nome)