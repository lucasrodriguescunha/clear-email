"""
Main module for email cleaner application
"""
from src.config import Config
from src.email_operations import delete_emails_by_year, delete_all_emails, show_remaining_emails
from src.imap_connection import connect_imap, login_imap, logout_imap
from src.user_interface import (
    get_user_choice,
    get_year_from_user,
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
            year = get_year_from_user()
            if year is None:
                display_cancelled_message()
                return

            deleted_ids = delete_emails_by_year(mail, year)
            if deleted_ids:
                display_result_message(len(deleted_ids), year)
        elif choice == '2':
            deleted_ids = delete_all_emails(mail)
            if deleted_ids:
                display_result_message(len(deleted_ids))

        # Show remaining emails
        show_remaining_emails(mail)

    except Exception as e:
        print(f"Erro ao processar e-mails: {e}")
    finally:
        if 'mail' in locals():
            logout_imap(mail)


if __name__ == "__main__":
    main()
