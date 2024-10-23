from email import Email

email = Email("Guilherme", "GDS", "Desafio E-mail", "Apenas um teste")

def main():
    email.exibir()
    email.encaminhar_email("guiteste@gmail.com", "teste@gmail.com")

if __name__ == "__main__":
    main()