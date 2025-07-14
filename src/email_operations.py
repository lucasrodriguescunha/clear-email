def fetch_emails(mail):
    mail.select('inbox')
    status, messages = mail.search(None, 'ALL')
    if status != 'OK':
        print(f"Erro ao buscar e-mails: {status}")
        return []
    return messages[0].split()


def fetch_emails_by_year(mail, year):
    try:
        mail.select('inbox')
        search_criteria = f'(SINCE "01-Jan-{year}" BEFORE "01-Jan-{year+1}")'
        status, messages = mail.search(None, search_criteria)

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


def delete_emails_by_year(mail, year):
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
    try:
        remaining_ids = fetch_emails(mail)
        print(f'Restam {len(remaining_ids)} e-mails na caixa de entrada.')
    except Exception as e:
        print(f'Erro ao buscar a quantidade de e-mails restantes: {e}')


def fetch_emails_by_date(mail, date_str):
    try:
        mail.select('inbox')
        # Converte a string de data para o formato correto
        from datetime import datetime
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        search_date = date_obj.strftime('%d-%b-%Y')

        # Busca e-mails da data específica
        search_criteria = f'(ON "{search_date}")'
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"Erro ao buscar e-mails da data {date_str}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado para a data {date_str}.')
            return []

        print(f'Encontrados {len(email_ids)} e-mails para a data {date_str}.')
        return email_ids
    except ValueError:
        print('Formato de data inválido. Use o formato DD/MM/AAAA')
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails da data {date_str}: {e}')
        return []


def delete_emails_by_date(mail, date_str):
    try:
        email_ids = fetch_emails_by_date(mail, date_str)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails da data {date_str} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails da data {date_str}: {e}')
        return []


def fetch_emails_between_dates(mail, start_date_str, end_date_str):
    try:
        mail.select('inbox')
        # Converte as strings de data para o formato correto
        from datetime import datetime
        start_date_obj = datetime.strptime(start_date_str, '%d/%m/%Y')
        end_date_obj = datetime.strptime(end_date_str, '%d/%m/%Y')

        # Verifica se a data inicial é anterior à data final
        if start_date_obj > end_date_obj:
            print('A data inicial deve ser anterior à data final')
            return []

        start_date = start_date_obj.strftime('%d-%b-%Y')
        end_date = end_date_obj.strftime('%d-%b-%Y')

        # Busca e-mails entre as datas específicas
        search_criteria = f'(SINCE "{start_date}" BEFORE "{end_date}")'
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"Erro ao buscar e-mails entre {start_date_str} e {end_date_str}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado entre {start_date_str} e {end_date_str}.')
            return []

        print(f'Encontrados {len(email_ids)} e-mails entre {start_date_str} e {end_date_str}.')
        return email_ids
    except ValueError:
        print('Formato de data inválido. Use o formato DD/MM/AAAA')
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails entre as datas: {e}')
        return []


def delete_emails_between_dates(mail, start_date_str, end_date_str):
    try:
        email_ids = fetch_emails_between_dates(mail, start_date_str, end_date_str)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails entre {start_date_str} e {end_date_str} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails entre as datas: {e}')
        return []


def fetch_emails_older_than(mail, date_str):
    try:
        mail.select('inbox')
        from datetime import datetime
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        search_date = date_obj.strftime('%d-%b-%Y')

        # Busca e-mails anteriores à data específica
        search_criteria = f'(BEFORE "{search_date}")'
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"Erro ao buscar e-mails anteriores a {date_str}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado anterior a {date_str}.')
            return []

        print(f'Encontrados {len(email_ids)} e-mails anteriores a {date_str}.')
        return email_ids
    except ValueError:
        print('Formato de data inválido. Use o formato DD/MM/AAAA')
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails anteriores à data: {e}')
        return []

def fetch_emails_newer_than(mail, date_str):
    try:
        mail.select('inbox')
        from datetime import datetime
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        search_date = date_obj.strftime('%d-%b-%Y')

        # Busca e-mails posteriores à data específica
        search_criteria = f'(SINCE "{search_date}")'
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"Erro ao buscar e-mails posteriores a {date_str}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado posterior a {date_str}.')
            return []

        print(f'Encontrados {len(email_ids)} e-mails posteriores a {date_str}.')
        return email_ids
    except ValueError:
        print('Formato de data inválido. Use o formato DD/MM/AAAA')
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails posteriores à data: {e}')
        return []

def fetch_emails_by_month_year(mail, month, year):
    try:
        mail.select('inbox')
        from datetime import datetime

        # Cria datas para início e fim do mês
        start_date = datetime(year, month, 1)
        # Se for dezembro, o próximo mês é janeiro do próximo ano
        next_month = 1 if month == 12 else month + 1
        next_year = year + 1 if month == 12 else year
        end_date = datetime(next_year, next_month, 1)

        start_date_str = start_date.strftime('%d-%b-%Y')
        end_date_str = end_date.strftime('%d-%b-%Y')

        # Busca e-mails do mês/ano específico
        search_criteria = f'(SINCE "{start_date_str}" BEFORE "{end_date_str}")'
        status, messages = mail.search(None, search_criteria)

        if status != 'OK':
            print(f"Erro ao buscar e-mails de {month:02d}/{year}: {status}")
            return []

        email_ids = messages[0].split()
        if not email_ids:
            print(f'Nenhum e-mail encontrado em {month:02d}/{year}.')
            return []

        print(f'Encontrados {len(email_ids)} e-mails em {month:02d}/{year}.')
        return email_ids
    except ValueError:
        print('Mês ou ano inválido.')
        return []
    except Exception as e:
        print(f'Erro ao buscar e-mails do mês/ano: {e}')
        return []

def delete_emails_older_than(mail, date_str):
    try:
        email_ids = fetch_emails_older_than(mail, date_str)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails anteriores a {date_str} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails anteriores à data: {e}')
        return []

def delete_emails_newer_than(mail, date_str):
    try:
        email_ids = fetch_emails_newer_than(mail, date_str)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails posteriores a {date_str} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails posteriores à data: {e}')
        return []

def delete_emails_by_month_year(mail, month, year):
    try:
        email_ids = fetch_emails_by_month_year(mail, month, year)
        if not email_ids:
            return []

        mark_for_deletion(mail, email_ids)
        expunge_emails(mail)
        print(f'Todos os e-mails de {month:02d}/{year} foram apagados com sucesso!')
        return email_ids
    except Exception as e:
        print(f'Erro ao excluir e-mails do mês/ano: {e}')
        return []
