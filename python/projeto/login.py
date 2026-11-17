import mod_msg
import mod_inputs

USUARIO = "wesney"
SENHA = "123456"

def valida_usuario(user):
    while True:
        usuario = mod_inputs.recebe_str("Digite o seu usuario: ")
        if len(usuario) >= 5:
            if user == usuario:
                break
            else:
                print("Usuario Incorreto!\n")
        else:
            print("O usuario deve conter mais de 5 digitos\n")
    return usuario

def valida_senha(password):
    while True:
        senha = mod_inputs.recebe_senha("Digite sua senha: ")
        if password == senha:
            break
        else:
            print("Senha inválida!\n")
    return senha

def main():
    mod_msg.msg_log_inicial()
    usuario_validado = valida_usuario(USUARIO)
    senha_validada = valida_senha(SENHA)
    print("\nLogin realizado com Sucesso! \nUsuario:",usuario_validado)
    print("Senha:",senha_validada)
        