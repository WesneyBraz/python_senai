import math
import mod_inputs
import mod_msg

def formula(y,x,z,w,d,embalagem):
    if(embalagem == 1):
        f = 0.37
        resultado = ((y*x*z*w)*(1+f))*(1+(d*9.8))
    else:
        f = 0.26
        resultado = ((y*x*z*w)*(1+f))*(1+(d*9.8))
    return resultado

def unidade_medida(embalagem):
    if embalagem == 1:
        unidade = "Metros"
    else:
        unidade = "Centímetros"
    return unidade

def distancia(aeroporto):
    match aeroporto:
        case 1:
            d = 102
        case 2:
            d = 112
        case 3:
            d = 98
        case 4:
            d = 2922
        case 5:
            d = 6294
        case _:
            print("valor invalido!")
    return d

def recebe_aeroporto():
    while True:
        aeroporto = mod_inputs.recebe_int("qual a sua escolha? ")
        if(aeroporto >0 and aeroporto <6):
            resultado = distancia(aeroporto)
            break
        else:
            print("Valor inválido!")
    return resultado

def recebe_embalagem():
    while True:
        embalagem = mod_inputs.recebe_int("qual a sua escolha? ")
        if(embalagem > 0 and embalagem <= 2):
            unidade = unidade_medida(embalagem)
            break
        else:
            print("Valor inválido!")
    return unidade

def main():
    mod_msg.msg_aeroporto_destino()
    d = recebe_aeroporto()

    mod_msg.msg_embalagem()
   
    mod_msg.msg_medidas(unidade)
    y = mod_inputs.recebe_float("Digite a altura: ")
    x = mod_inputs.recebe_float("Digite a largura: ")
    z = mod_inputs.recebe_float("Digite a profundidade: ")
    w = mod_inputs.recebe_float("Digite o peso: ")
    formula(y,x,z,w,d,embalagem)
    print("x:",x)
    print("y:",y)
    print("z:",z)
    print("w:",w)
