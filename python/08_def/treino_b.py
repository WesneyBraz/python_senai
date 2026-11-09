def calcular_media(num1,num2, num3):
    resultado = (num1 + num2 + num3)/3
    return resultado

def recebe_numero(mensagem):

    start = True
    while start:
        try:
            numero = float(input(mensagem).replace(",","."))

            start = False
        except:
            print("Entrada invalida, digite um número")
    return numero

def situacao(media):
    if (media>50):
        mensagem = "Aprovado"
    else:
        mensagem = "Reprovado"

    return mensagem

print("As notas são de 1 a 100")
num1 = recebe_numero("Digite a 1º nota")
num2 = recebe_numero("Digite a 2º nota")
num3 = recebe_numero("Digite a 3º nota")

media = calcular_media(num1,num2,num3)
print("A média é: ", media)
print("O aluno esta: ", situacao(media))

