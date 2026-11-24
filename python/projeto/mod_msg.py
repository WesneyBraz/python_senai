import pyfiglet

def msg_inicial():
    print("Seja bem vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format("COTA-FRETE", font="pagga")
    print(mensagem)

def msg_login_ini():
    print("##############################")
    print("<<<<<< LOGAR NO SISTEMA >>>>>>")
    print("##############################\n")

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2 #####\n")

def msg_calc_ini():
    print("##############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>>")
    print("##############################\n")


def msg_final_programa():
    print("##############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>>")
    print("##############################\n")

def msg_aeroporto_destino():
    print("Informe o Aeroporto de destino\n")
    print("1 p/ Congonhas-SP (102km) -- 2 p/ Guarulhos-SP (112km) -- 3 p/ Campo de Marte-SP -- 4 p/ Pinto Martins-CE (2922kM) -- 5 p/ Eduardo Gomes-AM (6294km)\n")

def msg_embalagem():
    print("Qual o tipo de embalagem ?\n 1 p/ Caixa de papelão -- 2 p/ Container  ")

def msg_medidas(unidade):
    print("Informe a altura (",unidade,"), Largura (",unidade,"), profundidade (",unidade,") e peso (Kg)")
