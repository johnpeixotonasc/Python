# Python avançado: função map

print ("\nDe forma básica:\n")
def dobro(x):
    return x*2

valor = 2 # Se tranformar a viriável valor em uma lista dará problema
print (dobro(valor))

print ("\n------------------------------------*------------------------------------\n")

print ("Utilizando a função map:")

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor) # Utilizando a função map para aplicar a função dobro e chamando a lista que quero obter o valor dobrado
valor_dobrado = list(valor_dobrado) # Utilizando a função list para transformar o resultado da variável valor_dobrado em uma lista

print (valor_dobrado)