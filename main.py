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


def delete_emails_by_year(mail, year):
    try:
        mail.select('inbox')
        status, messages = mail.search(None, f'(SINCE {year}-01-01 BEFORE {year + 1}-01-01)')
        if status != 'OK':
            print(f"Erro ao buscar e-mails do ano {year}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado para o ano {year}.')
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails do ano {year} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails do ano {year}: {e}')
        return []


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


def get_user_choice():
    while True:
        try:
            print('\nO que você deseja fazer? ')
            print('[1] - Apagar e-mails de um ano específico')
            print('[2] - Apagar todos os e-mails')
            print('[0] - Sair')

            choice = input('Digite sua escolha (0, 1 ou 2): ').strip()

            if choice in ['0', '1', '2']:
                return choice
            else:
                print('Opção inválida! Por favor, digite 0, 1 ou 2.')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            return '0'
        except Exception as e:
            print(f'Erro ao ler entrada do usuário: {e}')


def get_year_from_user():
    while True:
        try:
            year_input = input('Digite o ano (ex: 2020): ').strip()
            year = int(year_input)

            if 1990 <= year <= 2030:  # Validação básica do ano
                return year
            else:
                print('Ano inválido! Por favor, digite um ano entre 1990 e 2030.')
        except ValueError:
            print('Por favor, digite um ano válido (apenas números).')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            return None
        except Exception as e:
            print(f'Erro ao ler ano: {e}')


def delete_all_emails(mail):
    try:
        email_ids = fetch_emails(mail)
        if not email_ids:
            print('Nenhum e-mail encontrado na caixa de entrada.')
            return []

        print(f'Total de e-mails encontrados: {len(email_ids)}')

        # Confirmação antes de excluir todos
        confirm = input('Tem certeza que deseja excluir TODOS os e-mails? (digite "SIM" para confirmar): ').strip()
        if confirm.upper() != 'SIM':
            print('Operação cancelada.')
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir todos os e-mails: {e}')
        return []


def main():
    load_dotenv()

    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    IMAP_SERVER = os.getenv('IMAP_SERVER', 'imap.gmail.com')

    if not EMAIL or not PASSWORD:
        raise ValueError("As variáveis de ambiente EMAIL e PASSWORD devem ser definidas no arquivo .env.")

    print(f"Conectando ao servidor IMAP: {IMAP_SERVER}")
    mail = connect_imap(IMAP_SERVER)
    if not mail:
        return

    if not login_imap(mail, EMAIL, PASSWORD):
        return

    try:
        choice = get_user_choice()

        if choice == '0':
            print('Programa encerrado.')
            return
        elif choice == '1':
            year = get_year_from_user()
            if year is None:
                print('Operação cancelada.')
                return

            deleted_ids = delete_emails_by_year(mail, year)
            if deleted_ids:
                print(f'Total de {len(deleted_ids)} e-mails do ano {year} foram excluídos.')
        elif choice == '2':
            deleted_ids = delete_all_emails(mail)
            if deleted_ids:
                print(f'Total de {len(deleted_ids)} e-mails foram excluídos.')

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
