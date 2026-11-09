try:
    entrada = int(input("Digite um número inteiro para saber a sua tabuada de 1 a 10:"))
    contador = 1
    while contador<11:
        resultado = entrada * contador
        print(contador, "*", entrada, "=", resultado)
        contador+=1
except:
    print("Entrada inválida")

