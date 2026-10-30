try: 
    numero1 = int(input("Digite o 1º número: "))
    numero2 = int(input("Digite o 2º número: "))
    resultado = numero1 / numero2
    print("O valor da divisão de",numero1,"por", numero2, "é", resultado)

except ValueError:
    print("Entradas invalidas")

except ZeroDivisionError:
    print("O número 2 precisa ser maior do que 0")

        
