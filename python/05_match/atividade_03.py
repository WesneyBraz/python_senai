try:
    print(" Menu de operações bancarias \n")
    print("1 - Consultar saldo \n")
    print("2 - Depositar \n")
    print("3 - Sacar \n")
    print("4 - Sair \n")
    entrada = int(input("Escolha a operação que deseja realizar: "))

    saldo = 1000.00
    match entrada:
        case 1:
            print("O seu saldo atual é: ", saldo)
        case 2:
            deposito = float(input("Digite o valor a ser depositado: "))
            saldo_final = saldo + deposito
            print("O seu saldo atual é: ", saldo_final)
        case 3:
            saque = float(input("Digite o valor a ser sacado: "))
            if(saque>saldo):
                print("Valor acima do permitido")
            else:
                saldo_final = saldo - saque
                print("O seu saldo atual é: ", saldo_final)
        case 4:
            print("Saindo")
        case _: 
            print("Operação invalida")
except:
    print("Erro")