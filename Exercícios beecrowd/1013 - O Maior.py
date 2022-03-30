# 1013 - O Maior

linha = input().split() # seta todos os valores na mesma linha
a = int(linha[0]) # seta o valor a na posição 0
b = int(linha[1]) # seta o valor b na posição 1
c = int(linha[2]) # seta o valor c na posição 2
maior = max(a,b,c)
print("{} eh o maior".format(maior))
