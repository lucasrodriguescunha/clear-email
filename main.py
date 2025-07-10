import imaplib
import os

from dotenv import load_dotenv

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
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    except Exception as e:
        print(f"Erro ao conectar ao servidor IMAP: {e}")
        return

    try:
        mail.login(EMAIL, PASSWORD)
        print("Login realizado com sucesso!")
    except imaplib.IMAP4.error as e:
        print(f"Erro de autenticação: {e}")
        return
    except Exception as e:
        print(f"Erro inesperado ao fazer login: {e}")
        return

    try:
        mail.select('inbox')
        status, messages = mail.search(None, 'ALL')
        if status != 'OK':
            print(f"Erro ao buscar e-mails: {status}")
            return
        email_ids = messages[0].split()
        print(f'Total de e-mails encontrados: {len(email_ids)}')

        for idx, email_id in enumerate(email_ids, 1):
            try:
                mail.store(email_id, '+FLAGS', '\\Deleted')
                if idx % 100 == 0 or idx == len(email_ids):
                    print(f'{idx} de {len(email_ids)} e-mails marcados para exclusão...')
            except Exception as e:
                print(f'Erro ao tentar excluir o e-mail {email_id}: {e}')

        try:
            mail.expunge()
            print('Todos os e-mails foram apagados com sucesso!')
        except Exception as e:
            print(f'Erro ao remover e-mails: {e}')
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
