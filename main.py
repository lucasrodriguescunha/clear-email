"""
Main module for email cleaner application
"""
from src.config import Config
from src.email_operations import (
    delete_emails_by_year,
    delete_all_emails,
    show_remaining_emails,
    delete_emails_by_date,
    delete_emails_between_dates,
    delete_emails_older_than,
    delete_emails_newer_than,
    delete_emails_by_month_year
)
from src.imap_connection import connect_imap, login_imap, logout_imap
from src.user_interface import (
    get_user_choice,
    get_year_from_user,
    get_date_from_user,
    get_date_range_from_user,
    get_month_year_from_user,
    display_welcome_message,
    display_connection_message,
    display_result_message,
    display_exit_message,
    display_cancelled_message
)


def main():
    """Main function to run the email cleaner application"""
    try:
        # Display welcome message
        display_welcome_message()

        # Load configuration
        config = Config()
        config.validate_credentials()

        # Connect to IMAP server
        display_connection_message(config.get_imap_server())
        mail = connect_imap(config.get_imap_server())
        if not mail:
            return

        # Login to IMAP server
        if not login_imap(mail, config.get_email(), config.get_password()):
            return

        # Get user choice and process
        choice = get_user_choice()

        if choice == '0':
            display_exit_message()
            return
        elif choice == '1':
            date_str = get_date_from_user()
            if date_str is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_by_date(mail, date_str)
            if deleted_ids:
                display_result_message(len(deleted_ids))
        elif choice == '2':
            start_date, end_date = get_date_range_from_user()
            if start_date is None or end_date is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_between_dates(mail, start_date, end_date)
            if deleted_ids:
                display_result_message(len(deleted_ids))
        elif choice == '3':
            date_str = get_date_from_user()
            if date_str is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_older_than(mail, date_str)
            if deleted_ids:
                display_result_message(len(deleted_ids))
        elif choice == '4':
            date_str = get_date_from_user()
            if date_str is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_newer_than(mail, date_str)
            if deleted_ids:
                display_result_message(len(deleted_ids))
        elif choice == '5':
            month, year = get_month_year_from_user()
            if month is None or year is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_by_month_year(mail, month, year)
            if deleted_ids:
                display_result_message(len(deleted_ids))
        elif choice == '6':
            year = get_year_from_user()
            if year is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_by_year(mail, year)
            if deleted_ids:
                display_result_message(len(deleted_ids), year)
        elif choice == '7':
            deleted_ids = delete_all_emails(mail)
            if deleted_ids:
                display_result_message(len(deleted_ids))

        # Show remaining emails count
        show_remaining_emails(mail)

    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        if 'mail' in locals():
            logout_imap(mail)


if __name__ == "__main__":
    main()
