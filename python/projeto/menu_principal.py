import mod_msg
import mod_inputs

def decisao():
    while True:
        escolha = mod_inputs.recebe_int("Digite o número de sua escolha: ")
        match escolha:
            case 0:
                print("Sair")
                break
            case 1:
                print("Calculadora")
                break
            case 2:
                print("Calcula frete")
                break
            case _: 
                print("Operação invalida")
    return escolha

def main():
    mod_msg.msg_menu_principal()
    decisao()
