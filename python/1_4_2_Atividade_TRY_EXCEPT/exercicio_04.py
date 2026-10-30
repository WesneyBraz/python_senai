try:
    nota1 = float(input("Digite a 1º nota: "))
    nota2 = float(input("Digite a 2º nota: "))
    nota3 = float(input("Digite a 3º nota: "))
    media = (nota1 + nota2 + nota3)/3
    print("A sua média é:", media)
    if media>=70:
        print("Aprovado")
    else:
        print("Reprovado")
except ValueError:
    print("Entrada inválidas")