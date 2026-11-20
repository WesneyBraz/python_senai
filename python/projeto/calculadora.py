import mod_msg
import mod_inputs

def valida_operador():
    while True:
        print("Digite + para ADIÇÃO")
        print("Digite - para SUBTRAÇÃO")
        print("Digite * para MULTIPLICAÇÃO")
        print("Digite / para DIVISÃO")
        print("Digite % para PORCENTAGEM")
        operador = mod_inputs.recebe_str("Digite a sua escolha")
        if operador in("*", "/", "+", "-", "%"):
            break
        else:
            print("\nOperador inválido!\n")
    return operador

def realiza_calculo(numero1,numero2,operador):
    match operador:
        case "+":
            resultado = numero1+numero2
        case "-":
            resultado = numero1-numero2
        case "*":
            resultado = numero1*numero2
        case "/":
            resultado = numero1/numero2
        case "%":
            resultado = (numero1 * numero2)/100
    return resultado

def main():
    mod_msg.msg_calculadora()
    numero1 = mod_inputs.recebe_float("Digite o 1º número: ")
    numero2 = mod_inputs.recebe_float("Digite o 2º número: ")
    operador = valida_operador()

if __name__ == "main"():
    main()