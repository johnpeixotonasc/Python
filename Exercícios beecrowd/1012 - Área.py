# 1012 - Área

linha1 = input().split()
A = float(linha1[0])
B = float(linha1[1])
C = float(linha1[2])
pi = 3.14159

# a área do triângulo retângulo que tem A por base e C por altura.
triangulo = (A*C)/2
print("TRIANGULO: {:.3f}".format(triangulo))

# a área do círculo de raio C. (pi = 3.14159)
circulo = pi*(pow(C,2))
print("CIRCULO: {:.3f}".format(circulo))

# a área do trapézio que tem A e B por bases e C por altura.
trapezio = ((A+B)*C)/2
print("TRAPEZIO: {:.3f}".format(trapezio))

# a área do quadrado que tem lado B.
quadrado = B*B
print("QUADRADO: {:.3f}".format(quadrado))

# a área do retângulo que tem lados A e B
retangulo = A*B
print("RETANGULO: {:.3f}".format(retangulo))