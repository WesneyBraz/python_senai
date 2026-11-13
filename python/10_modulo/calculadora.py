import mod_sair
import mod_inputs
import operacoes

def processa(operacao, numero1, numero2):
    while True:

        match operacao:
            case "+":
                resultado = operacoes.somar(numero1,numero2)

            case "-":
                resultado = operacoes.subtrair(numero1,numero2)

            case "*":
                resultado = operacoes.multiplicar(numero1,numero2)

            case "/":
                resultado = operacoes.dividir(numero1,numero2)
            case _: 
                print("Operador invalido!")
        return resultado

def mensagem_inicial():
    print("Digite 2 números e escolha operação a ser realizada")
    print("\n + para soma \n - para subtração \n * para multiplicação \n / para divisão")

decisao = True 
while decisao:
   
    mensagem_inicial()
    numero1 = mod_inputs.input_float("Digite o 1º número: ")
    numero2 = mod_inputs.input_float("Digite o 2º número: ")
    operacao = mod_inputs.input_str("qual operação? ")
    resultado = processa(operacao,numero1,numero2)
    
    print("Resultado da operacao: ", resultado)

    decisao = mod_sair.finalizar()