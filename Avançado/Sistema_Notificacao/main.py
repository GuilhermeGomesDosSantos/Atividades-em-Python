from Notificação import Notificacao

notificacao_1 = Notificacao()


def main():
    # notificacao_1.enviar_email()
    # notificacao_1.enviar_sms()
    notificacao_1.enviar_push()

if __name__ == "__main__":
    main()