#Atividade Prática Python - Input I/O
#08 atividade_08.py 
#Crie um programa capaz de calcular a velocidade média de um veíoculo. considere a fórmula da velocidade média abaixo: 
#Velocidade Média = Distância / Tempo

distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

if tempo != 0:
    velocidade_media = distancia / tempo
    print("A velocidade média do veículo é:", velocidade_media, "km/h")
else:
    print("O tempo não pode ser zero.")