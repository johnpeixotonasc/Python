# 1017 - Gasto de Combustível

temp_gasto = int(input())
vel_media = int(input())

km_plitro = (temp_gasto * vel_media)/12.0

print("{:.3f}".format(km_plitro))