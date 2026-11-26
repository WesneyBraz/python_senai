#Atividade Prática Python - Input I/O
#09 atividade_09.py 
#Crie um programa capaz de calcular a força gravitacional (Força G) entre 2 (dois) corpos. Considere a fórmula da força gravitacional
#Lei da Gravitação Universal de Newton: F = G * (m1 * m2) / d^2.

G = 6.67 * 10**-11 
m1 = float(input("Digite a massa do primeiro corpo (em kg): "))
m2 = float(input("Digite a massa do segundo corpo (em kg): "))  
d = float(input("Digite a distância entre os corpos (em metros): "))
if d != 0:
    F = G * (m1 * m2) / d**2
    print("A força gravitacional entre os corpos é:", F, "N")
else:
    print("A distância entre os corpos não pode ser zero.")