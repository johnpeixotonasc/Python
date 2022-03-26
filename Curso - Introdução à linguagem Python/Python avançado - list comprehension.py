# Python avançado: list comprehension

x = [1, 2, 3, 4, 5]
y = []

print ("\nInserindo a raiz quadrada usando append:\n")
for i in x:
    y.append(i**2) 
print (x)
print (y)

print ("\n------------------------------------*------------------------------------\n")

print ("\nInserindo a raiz quadrada usando list comprehension:\n")

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

print (x)
print (y)

print ("\n------------------------------------*------------------------------------\n")

print ("\nInserindo a raiz quadrada usando condição:\n")

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print (x)
print (y)
print (z)