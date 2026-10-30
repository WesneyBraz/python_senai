try:
    print("Informe seus dados")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Entrada invalida")