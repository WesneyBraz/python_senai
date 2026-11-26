#Atividade Prática Python - Input I/O
#10 atividade_10.py 
#Crie um programa que apoie o setor de elétrica onde seja possível informar o disjuntor adequado para instalação de um chuveiro.
#lembre-se que o disjuntor é indicado pela amperagem do chuveiro + 10% de margem de sobra.

potencia = float(input("Digite a potencia do chuveiro (em W): "))    
tensao = float(input("Digite a tensão do chuveiro (em V): "))
amperagem_chuveiro = potencia / tensao
amperagem_disjuntor = amperagem_chuveiro * 1.1
print("A amperagem do disjuntor adequado é:", amperagem_disjuntor, "A")