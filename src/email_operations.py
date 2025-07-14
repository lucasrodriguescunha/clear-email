from datetime import datetime

DATE_FORMAT = '%d/%m/%Y'
IMAP_DATE_FORMAT = '%d-%b-%Y'
INVALID_DATE_FORMAT_MSG = 'Formato de data inválido. Use o formato DD/MM/AAAA'
INVALID_MONTH_YEAR_MSG = 'Mês ou ano inválido.'

def convert_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, DATE_FORMAT)
        return date_obj.strftime(IMAP_DATE_FORMAT)
    except ValueError:
        print(INVALID_DATE_FORMAT_MSG)
        return None

def fetch_and_process_emails(mail, search_criteria, error_msg):
    try:
        mail.select('inbox')
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"{error_msg}: {status}")
            return []

        email_ids = messages[0].split()
        return email_ids
    except Exception as e:
        print(f"{error_msg}: {e}")
        return []

def fetch_emails(mail):
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    if status != 'OK':
        print(f"Erro ao buscar e-mails: {status}")
        return []
    return messages[0].split()

# Funções auxiliares de manipulação de e-mails
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

def delete_emails_with_confirmation(mail, email_ids, success_msg):
    try:
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(success_msg)
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails: {e}')
        return []

# Funções de busca de e-mails
def fetch_emails_by_criteria(mail, date_str, criteria_type):
    try:
        search_date = convert_date(date_str)
        if not search_date:
            return []

        criteria_map = {
            'on': (f'(ON "{search_date}")', 'da data', 'para a data'),
            'before': (f'(BEFORE "{search_date}")', 'anteriores a', 'anterior a'),
            'since': (f'(SINCE "{search_date}")', 'posteriores a', 'posterior a')
        }

        if criteria_type not in criteria_map:
            print(f'Tipo de critério inválido: {criteria_type}')
            return []

        search_criteria, msg_prefix, msg_suffix = criteria_map[criteria_type]
        email_ids = fetch_and_process_emails(
            mail,
            search_criteria,
            f"Erro ao buscar e-mails {msg_prefix} {date_str}"
        )

        if email_ids:
            print(f'Encontrados {len(email_ids)} e-mails {msg_prefix} {date_str}.')
        else:
            print(f'Nenhum e-mail encontrado {msg_suffix} {date_str}.')

        return email_ids
    except Exception as e:
        print(f'Erro ao buscar e-mails por critério: {e}')
        return []

def fetch_emails_by_date(mail, date_str):
    return fetch_emails_by_criteria(mail, date_str, 'on')

def fetch_emails_between_dates(mail, start_date_str, end_date_str):
    try:
        start_date = convert_date(start_date_str)
        end_date = convert_date(end_date_str)
        if not start_date or not end_date:
            return []

        search_criteria = f'(SINCE "{start_date}" BEFORE "{end_date}")'
        date_range = f'{start_date_str} e {end_date_str}'
        email_ids = fetch_and_process_emails(
            mail,
            search_criteria,
            f"Erro ao buscar e-mails entre {date_range}"
        )

        if email_ids:
            print(f'Encontrados {len(email_ids)} e-mails entre {date_range}.')
        else:
            print(f'Nenhum e-mail encontrado entre {date_range}.')

        return email_ids
    except Exception as e:
        print(f'Erro ao buscar e-mails entre as datas: {e}')
        return []

def fetch_emails_older_than(mail, date_str):
    return fetch_emails_by_criteria(mail, date_str, 'before')

def fetch_emails_newer_than(mail, date_str):
    return fetch_emails_by_criteria(mail, date_str, 'since')

def fetch_emails_by_month_year(mail, month, year):
    try:
        start_date = datetime(year, month, 1)
        next_month = 1 if month == 12 else month + 1
        next_year = year + 1 if month == 12 else year
        end_date = datetime(next_year, next_month, 1)

        search_criteria = f'(SINCE "{start_date.strftime(IMAP_DATE_FORMAT)}" BEFORE "{end_date.strftime(IMAP_DATE_FORMAT)}")'
        period = f'{month:02d}/{year}'
        email_ids = fetch_and_process_emails(
            mail,
            search_criteria,
            f"Erro ao buscar e-mails de {period}"
        )

        if email_ids:
            print(f'Encontrados {len(email_ids)} e-mails em {period}.')
        else:
            print(f'Nenhum e-mail encontrado em {period}.')

        return email_ids
    except ValueError:
        print(INVALID_MONTH_YEAR_MSG)
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails do mês/ano: {e}')
        return []

# Funções de exclusão de e-mails
def delete_emails_by_date(mail, date_str):
    email_ids = fetch_emails_by_date(mail, date_str)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails da data {date_str} foram apagados com sucesso!'
    )

def delete_emails_between_dates(mail, start_date_str, end_date_str):
    email_ids = fetch_emails_between_dates(mail, start_date_str, end_date_str)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails entre {start_date_str} e {end_date_str} foram apagados com sucesso!'
    )

def delete_emails_older_than(mail, date_str):
    email_ids = fetch_emails_older_than(mail, date_str)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails anteriores a {date_str} foram apagados com sucesso!'
    )

def delete_emails_newer_than(mail, date_str):
    email_ids = fetch_emails_newer_than(mail, date_str)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails posteriores a {date_str} foram apagados com sucesso!'
    )

def delete_emails_by_month_year(mail, month, year):
    email_ids = fetch_emails_by_month_year(mail, month, year)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails de {month:02d}/{year} foram apagados com sucesso!'
    )

def delete_emails_by_year(mail, year):
    email_ids = fetch_emails_by_month_year(mail, 1, year)
    return delete_emails_with_confirmation(
        mail,
        email_ids,
        f'Todos os e-mails do ano {year} foram apagados com sucesso!'
    )

def delete_all_emails(mail):
    try:
        email_ids = fetch_emails(mail)
        if not email_ids:
            print('Nenhum e-mail encontrado na caixa de entrada.')
            return []

        print(f'Total de e-mails encontrados: {len(email_ids)}')

        confirm = input('Tem certeza que deseja excluir TODOS os e-mails? (digite "SIM" para confirmar): ').strip()
        if confirm.upper() != 'SIM':
            print('Operação cancelada.')
            return []

        return delete_emails_with_confirmation(
            mail,
            email_ids,
            'Todos os e-mails foram apagados com sucesso!'
        )
    except Exception as e:
        print(f'Erro ao excluir todos os e-mails: {e}')
        return []

def show_remaining_emails(mail):
    try:
        remaining_ids = fetch_emails(mail)
        print(f'Restam {len(remaining_ids)} e-mails na caixa de entrada.')
    except Exception as e:
        print(f'Erro ao buscar a quantidade de e-mails restantes: {e}')
