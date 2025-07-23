from src.config import Config
from src.email_operations import (
    delete_emails_by_year,
    delete_all_emails,
    show_remaining_emails,
    delete_emails_by_date,
    delete_emails_between_dates,
    delete_emails_older_than,
    delete_emails_newer_than,
    delete_emails_by_month_year,
    delete_emails_by_subject_keywords
)
from src.imap_connection import connect_imap, login_imap, logout_imap
from src.user_interface import (
    get_user_choice,
    get_year_from_user,
    get_date_from_user,
    get_date_range_from_user,
    get_month_year_from_user,
    get_keywords_from_user,
    add_more_keywords,
    display_welcome_message,
    display_connection_message,
    display_result_message,
    display_exit_message,
    display_cancelled_message
)


def initialize_connection(config):
    display_connection_message(config.get_imap_server())
    mail = connect_imap(config.get_imap_server())
    if not mail:
        return None

    if not login_imap(mail, config.get_email(), config.get_password()):
        return None

    return mail


def handle_single_date_operation(mail, operation_func, get_date=True):
    if get_date:
        date_str = get_date_from_user()
        if date_str is None:
            display_cancelled_message()
            return False
    else:
        year = get_year_from_user()
        if year is None:
            display_cancelled_message()
            return False
        date_str = year

    deleted_ids = operation_func(mail, date_str)
    if deleted_ids:
        display_result_message(len(deleted_ids))
    return True


def handle_date_range_operation(mail):
    start_date, end_date = get_date_range_from_user()
    if start_date is None or end_date is None:
        display_cancelled_message()
        return False

    deleted_ids = delete_emails_between_dates(mail, start_date, end_date)
    if deleted_ids:
        display_result_message(len(deleted_ids))
    return True


def handle_month_year_operation(mail):
    month, year = get_month_year_from_user()
    if month is None or year is None:
        display_cancelled_message()
        return False

    deleted_ids = delete_emails_by_month_year(mail, month, year)
    if deleted_ids:
        display_result_message(len(deleted_ids))
    return True


def handle_all_emails_operation(mail):
    deleted_ids = delete_all_emails(mail)
    if deleted_ids:
        display_result_message(len(deleted_ids))
    return True


def handle_keywords_operation(mail):
    keywords = get_keywords_from_user()
    if keywords is None:
        display_cancelled_message()
        return False

    # Permitir adicionar mais palavras-chave
    final_keywords = add_more_keywords(keywords)

    deleted_ids = delete_emails_by_subject_keywords(mail, final_keywords)
    if deleted_ids:
        display_result_message(len(deleted_ids))
    return True


def process_user_choice(mail, choice):
    operations = {
        '0': lambda: False,
        '1': lambda: handle_single_date_operation(mail, delete_emails_by_date),
        '2': lambda: handle_date_range_operation(mail),
        '3': lambda: handle_single_date_operation(mail, delete_emails_older_than),
        '4': lambda: handle_single_date_operation(mail, delete_emails_newer_than),
        '5': lambda: handle_month_year_operation(mail),
        '6': lambda: handle_single_date_operation(mail, delete_emails_by_year, False),
        '7': lambda: handle_keywords_operation(mail),
        '8': lambda: handle_all_emails_operation(mail)
    }

    if choice == '0':
        display_exit_message()
        return False

    operation = operations.get(choice)
    if operation:
        return operation()
    return True


def main():
    mail = None
    try:
        display_welcome_message()

        config = Config()
        config.validate_credentials()

        mail = initialize_connection(config)
        if not mail:
            return

        while True:
            choice = get_user_choice()
            if not process_user_choice(mail, choice):
                break
            show_remaining_emails(mail)

    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        if mail:
            logout_imap(mail)


if __name__ == "__main__":
    main()
