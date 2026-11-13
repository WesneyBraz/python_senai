import mod_formulas
import mod_sair

decisao = True
while decisao:
    try:
        raio = float(input("Digite o valor do raio: ").replace(",","."))
        calculo = mod_formulas.circunferencia(raio)
        print("Circunferência: ", calculo)
    except:
        print("Entrada inválida")

    decisao = mod_sair.finalizar()