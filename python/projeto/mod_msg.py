import pyfiglet

def msg_inicial():
    print("\nSeja bem vindo ao Sistema\n")
    mensagem =  pyfiglet.figlet_format("COTA\nFRETE", font="larry3d") 
    print(mensagem)

def msg_log_inicial():
    print("=======================================\n")
    print("<<<<<<< -- LOGAR NO SITEMA -- >>>>>>>>>\n")
    print("=======================================\n")

def msg_menu_principal():
    print("===============================================================\n")
    print("#################### -- MENU PRINCIPAL -- #####################\n")
    print("===============================================================\n")
    print("####### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2  ########\n")

def msg_calculadora():
    print("Calculadora")