
import mod_inputs
import mod_sair
import math

def imc(peso,altura):
    resultado = (peso/math.pow(altura,2))
    return round(resultado,2)

def classificacao(resultado,idade):
    if(idade<60):
        if (resultado<18.5):
            classificacao = "Baixo peso!"
        elif (resultado>=18.5 and resultado<=24.99):
            classificacao = "Normal!"
        elif (resultado>=25 and resultado<=29.99):
            classificacao = "Sobrepeso!"
        else:
            classificacao = "Obesidade!"
    else:
        if (resultado<22):
            classificacao = "Baixo peso!"
        elif (resultado>=22 and resultado<=27):
            classificacao = "Normal!"
        elif (resultado>=27.1 and resultado<=29.99):
            classificacao = "Sobrepeso!"
        else:
            classificacao = "Obesidade!"
    return classificacao

def exibir(nome,imc,idade,classicicacao):
    print("\n",nome,"para sua idade atual:",idade)
    print("Seu IMC atual é:",imc,"isso é classificado como:",classicicacao)

decisao = True
while decisao:
    nome = mod_inputs.input_str("Digite seu nome: ")
    altura = mod_inputs.input_float("Digite sua altura em metros: ")
    peso = mod_inputs.input_float("Digite seu peso em Kg: ")
    idade = mod_inputs.input_int("Digite a sua idade: ")

    resultado = imc(peso,altura)
    classificacao_final = classificacao(resultado,idade)

    exibir(nome,resultado,idade,classificacao_final)

    decisao = mod_sair.finalizar()