"""
IMAP connection module for email cleaner application
"""
import imaplib


def connect_imap(imap_server):
    """
    Connect to IMAP server

    Args:
        imap_server (str): IMAP server address

    Returns:
        imaplib.IMAP4_SSL: IMAP connection object or None if failed
    """
    try:
        return imaplib.IMAP4_SSL(imap_server)
    except Exception as e:
        print(f"Erro de conexão IMAP: {e}")
        return None


def login_imap(mail, email, password):
    """
    Login to IMAP server

    Args:
        mail: IMAP connection object
        email (str): Email address
        password (str): Password

    Returns:
        bool: True if login successful, False otherwise
    """
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
    """
    Logout from IMAP server

    Args:
        mail: IMAP connection object
    """
    try:
        mail.logout()
        print("Logout realizado com sucesso.")
    except Exception as e:
        print(f"Erro ao desconectar: {e}")
