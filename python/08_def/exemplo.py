def recebe_nome():
    nome = input("Digite o seu nome: ")
    return nome 

nome_verdadeiro = ""

while nome_verdadeiro != "wesney":
    retorno = recebe_nome()
    print("O nome informado é:",retorno)
    if(retorno == "wesney"):
        nome_verdadeiro = retorno

    print("debug_1:",retorno)
    print("debug_2:",nome_verdadeiro)
print("saiu")