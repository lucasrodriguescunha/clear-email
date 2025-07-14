"""
User interface module for email cleaner application
"""


def get_user_choice():
    """
    Get user choice for email deletion option

    Returns:
        str: User choice ('0', '1', '2', or '3')
    """
    while True:
        try:
            print('\nO que você deseja fazer? ')
            print('[1] - Apagar e-mails de uma data específica')
            print('[2] - Apagar e-mails de um ano específico')
            print('[3] - Apagar todos os e-mails')
            print('[0] - Sair')

            choice = input('Digite sua escolha (0, 1, 2 ou 3): ').strip()

            if choice in ['0', '1', '2', '3']:
                return choice
            else:
                print('Opção inválida! Por favor, digite 0, 1, 2 ou 3.')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            return '0'
        except Exception as e:
            print(f'Erro ao ler entrada do usuário: {e}')


def get_year_from_user():
    """
    Get year from user for email deletion

    Returns:
        int or None: Year entered by user or None if cancelled
    """
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


def get_date_from_user():
    """
    Get specific date from user for email deletion

    Returns:
        str or None: Date in DD/MM/YYYY format or None if cancelled
    """
    while True:
        try:
            date_input = input('Digite a data (DD/MM/AAAA): ').strip()
            from datetime import datetime
            # Verifica se a data está no formato correto
            datetime.strptime(date_input, '%d/%m/%Y')
            return date_input
        except ValueError:
            print('Data inválida! Use o formato DD/MM/AAAA (exemplo: 25/12/2023)')
        except KeyboardInterrupt:
            print('\nOperação cancelada pelo usuário.')
            return None
        except Exception as e:
            print(f'Erro ao ler data: {e}')


def display_welcome_message():
    """Display welcome message"""
    print("=" * 22)
    print("     CLEAR E-MAIL")
    print("=" * 22)


def display_connection_message(imap_server):
    """
    Display connection message

    Args:
        imap_server (str): IMAP server address
    """
    print(f"Conectando ao servidor IMAP: {imap_server}")


def display_result_message(deleted_count, year=None):
    """
    Display result message after deletion

    Args:
        deleted_count (int): Number of deleted emails
        year (int, optional): Year if deleting by year
    """
    if year:
        print(f'Total de {deleted_count} e-mails do ano {year} foram excluídos.')
    else:
        print(f'Total de {deleted_count} e-mails foram excluídos.')


def display_exit_message():
    """Display exit message"""
    print('Programa encerrado.')


def display_cancelled_message():
    """Display cancelled operation message"""
    print('Operação cancelada.')
