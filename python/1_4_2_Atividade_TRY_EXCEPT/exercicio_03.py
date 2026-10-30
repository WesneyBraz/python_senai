try:
    produto = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    percentual = int(input("Digite o valor de desconto: "))
    desconto = (preco*percentual)/100
    valor = preco - desconto
    print("Valor final do ",produto," é ",valor)
except:
    print("Entrada invalida")