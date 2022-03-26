# Python avançado: função zip

# A função zip concatena as listas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate -", "bola -", "cachorro -", "dinheiro -", "elefante -"]
lista3 = ["R$ 2,00", "R$ 5,00", "Não tem preço", "Não tem preço", "não tem preço"]


for numero, nome, valor in zip(lista1, lista2, lista3): # com a função zip ele irá concatenar a lista 1 com a lista 2
    print (numero, nome, valor)