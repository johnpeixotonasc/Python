# 1010 - Cálculo Simples

linha1 = input().split()
c1 = float(linha1[0])
n1 = float(linha1[1])
v1 = float(linha1[2])
linha2 = input().split()
c2 = float(linha2[0])
n2 = float(linha2[1])
v2 = float(linha2[2])
s = (n1*v1)+(n2*v2)
print("VALOR A PAGAR: R$ {:.2f}".format(s))