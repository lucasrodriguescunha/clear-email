import imaplib


def connect_imap(imap_server):
    try:
        return imaplib.IMAP4_SSL(imap_server)
    except Exception as e:
        print(f"Erro de conexão IMAP: {e}")
        return None


def login_imap(mail, email, password):
    try:
        mail.login(email, password)
        print("Login realizado com sucesso!")
        return True
    except imaplib.IMAP4.error as e:
        print(f"Erro de autenticação: {e}")
    except Exception as e:
        print(f"Erro inesperado ao fazer login: {e}")
    return False


def logout_imap(mail):
    try:
        mail.close()
        mail.logout()
        print("Logout realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao fazer logout: {e}")
