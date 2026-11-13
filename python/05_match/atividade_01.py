try:
    numero1 = float(input("Digite o primeiro número: ").replace(",", "."))
except:
    print("Entrada inválida. Por favor, digite um número válido.")

try:
    numero2 = float(input("Digite o segundo número: ").replace(",", "."))
except:
    print("Entrada inválida. Por favor, digite um número válido.")

try:
    print("Escolha uma das operações a seguir: \n")
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão") 
    operador = input("Digite o operador desejado: ")
except:
    print("Entrada inválida. Por favor, digite um operador válido.")

match operador:
    case "+":
        resultado = numero1 + numero2
        print(numero1, operador, numero2, "o resultado é:", resultado)
    case "-":
        resultado = numero1 - numero2
        print(numero1, operador, numero2, "o resultado é:", resultado)
    case "*":
        resultado = numero1 * numero2
        print(numero1, operador, numero2, "o resultado é:", resultado)
    case "/":
        resultado = numero1 / numero2
        print(numero1, operador, numero2, "o resultado é:", resultado)
    case _: 
        print("Operador invalido!")
