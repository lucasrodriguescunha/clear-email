"""
Email operations module for email cleaner application
"""


def fetch_emails(mail):
    """
    Fetch all emails from inbox

    Args:
        mail: IMAP connection object

    Returns:
        list: List of email IDs
    """
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    if status != 'OK':
        print(f"Erro ao buscar e-mails: {status}")
        return []
    return messages[0].split()


def fetch_emails_by_year(mail, year):
    """
    Fetch emails from a specific year

    Args:
        mail: IMAP connection object
        year (int): Year to search emails

    Returns:
        list: List of email IDs from the specified year
    """
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

        return email_ids
    except Exception as e:
        print(f'Erro ao buscar e-mails do ano {year}: {e}')
        return []


def mark_for_deletion(mail, email_ids):
    """
    Mark emails for deletion

    Args:
        mail: IMAP connection object
        email_ids (list): List of email IDs to mark for deletion
    """
    for idx, email_id in enumerate(email_ids, 1):
        try:
            mail.store(email_id, '+FLAGS', '\\Deleted')
            if idx % 100 == 0 or idx == len(email_ids):
                print(f'{idx} de {len(email_ids)} e-mails marcados para exclusão...')
        except Exception as e:
            print(f'Erro ao tentar excluir o e-mail {email_id}: {e}')


def expunge_emails(mail):
    """
    Permanently delete marked emails

    Args:
        mail: IMAP connection object
    """
    try:
        mail.expunge()
        print('Todos os e-mails foram apagados com sucesso!')
    except Exception as e:
        print(f'Erro ao remover e-mails: {e}')


def delete_emails_by_year(mail, year):
    """
    Delete all emails from a specific year

    Args:
        mail: IMAP connection object
        year (int): Year to delete emails from

    Returns:
        list: List of deleted email IDs
    """
    try:
        email_ids = fetch_emails_by_year(mail, year)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails do ano {year} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails do ano {year}: {e}')
        return []


def delete_all_emails(mail):
    """
    Delete all emails in the inbox

    Args:
        mail: IMAP connection object

    Returns:
        list: List of deleted email IDs
    """
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


def show_remaining_emails(mail):
    """
    Show count of remaining emails

    Args:
        mail: IMAP connection object
    """
    try:
        remaining_ids = fetch_emails(mail)
        print(f'Restam {len(remaining_ids)} e-mails na caixa de entrada.')
    except Exception as e:
        print(f'Erro ao buscar a quantidade de e-mails restantes: {e}')
