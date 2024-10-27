from Usuario import Usuario

user = Usuario("Guilherme", 123321, "teste@gmail.com")

def main():
    # user.autenticacao("teste@gmail.com",123321)
    user.atualizar_senha("abc")

if __name__ == "__main__":
    main()