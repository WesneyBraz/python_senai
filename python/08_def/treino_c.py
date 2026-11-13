def calcular_desconto(preco, percentual):
    desconto = (preco*percentual)/100
    return desconto

try:
    preco = float(input("Digite o preço do produto: ").replace(",","."))
    percentual = float(input("Digite o percentual do desconto: ").replace(",","."))

    resultado = calcular_desconto(preco, percentual)
    
except:
    print("Entrada inválida")