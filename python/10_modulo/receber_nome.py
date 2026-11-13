import mod_inputs
import mod_sair

decisao = True
while decisao:

    nome = mod_inputs.input_str("Digite seu nome: ")
    idade = mod_inputs.input_int("Digite a sua idade: ")
    peso = mod_inputs.input_float("Digite o seu peso: ")

    print("\n ============= Informações =============\n", "Nome: ",nome," - Idade: ", idade," - Peso: ", peso)

    decisao = mod_sair.finalizar()

print("\n ============= Adeus =============")