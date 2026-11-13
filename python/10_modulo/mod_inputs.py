import operacoes

def input_str(mensagem):
    while True:
        try:
            texto = str(input(mensagem))
            break
        except:
            print("Valor inválido, por favor digite um texto.")
    return texto

def input_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except:
            print("Valor inválido, por favor digite um numero.")
    return numero

def input_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem).replace(",","."))
            break
        except:
            print("Valor inválido, por favor digite um numero.")
    return numero


            