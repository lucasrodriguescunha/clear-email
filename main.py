import imaplib
import os

from dotenv import load_dotenv

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


def fetch_emails(mail):
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    if status != 'OK':
        print(f"Erro ao buscar e-mails: {status}")
        return []
    return messages[0].split()


def mark_for_deletion(mail, email_ids):
    for idx, email_id in enumerate(email_ids, 1):
        try:
            mail.store(email_id, '+FLAGS', '\\Deleted')
            if idx % 100 == 0 or idx == len(email_ids):
                print(f'{idx} de {len(email_ids)} e-mails marcados para exclusão...')
        except Exception as e:
            print(f'Erro ao tentar excluir o e-mail {email_id}: {e}')


def expunge_emails(mail):
    try:
        mail.expunge()
        print('Todos os e-mails foram apagados com sucesso!')
    except Exception as e:
        print(f'Erro ao remover e-mails: {e}')


def show_remaining_emails(mail):
    try:
        remaining_ids = fetch_emails(mail)
        print(f'Restam {len(remaining_ids)} e-mails na caixa de entrada.')
    except Exception as e:
        print(f'Erro ao buscar a quantidade de e-mails restantes: {e}')


def main():
    # Carregar variáveis do .env
    load_dotenv()

    # Configurações
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    IMAP_SERVER = os.getenv('IMAP_SERVER', 'imap.gmail.com')

    # Verificar se as credenciais foram carregadas
    if not EMAIL or not PASSWORD:
        raise ValueError("As variáveis de ambiente EMAIL e PASSWORD devem ser definidas no arquivo .env.")

    print(f"Conectando ao servidor IMAP: {IMAP_SERVER}")
    mail = connect_imap(IMAP_SERVER)
    if not mail:
        return

    if not login_imap(mail, EMAIL, PASSWORD):
        return

    try:
        email_ids = fetch_emails(mail)
        print(f'Total de e-mails encontrados: {len(email_ids)}')

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        show_remaining_emails(mail)
    except Exception as e:
        print(f"Erro ao processar e-mails: {e}")
    finally:
        try:
            mail.logout()
            print("Logout realizado com sucesso.")
        except Exception as e:
            print(f"Erro ao desconectar: {e}")


if __name__ == "__main__":
    main()
