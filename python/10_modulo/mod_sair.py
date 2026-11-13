from mod_inputs import input_str

def finalizar():
 
    while True:
        try:
            opcao = input_str("\n Deseja finalizar o programa ? Digite S para [SIM] ou N para [Não] ")
            if opcao in ("s", "S") or opcao in("n","N"):
                break
            else:
                print("\n Opção inválida")
        except:
            print("inválido")
    if opcao in("s","S"):
        print("\n ============= finalizado programa =============")
        return False
    else:
        return True
