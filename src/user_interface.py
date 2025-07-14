OPERATION_CANCELLED_MSG = '\nOperação cancelada pelo usuário.'
INVALID_YEAR_MSG = 'Ano inválido! Por favor, digite um ano entre 1990 e 2030.'
INVALID_MONTH_MSG = 'Mês inválido! Digite um número entre 1 e 12.'
INVALID_DATE_FORMAT_MSG = 'Data inválida! Use o formato DD/MM/AAAA (exemplo: 25/12/2023)'
INVALID_OPTION_MSG = 'Opção inválida! Por favor, digite um número entre 0 e 7.'


def get_user_choice():
    while True:
        try:
            print('\nO que você deseja fazer? ')
            print('[1] - Apagar e-mails de uma data específica')
            print('[2] - Apagar e-mails entre duas datas')
            print('[3] - Apagar e-mails anteriores a uma data')
            print('[4] - Apagar e-mails posteriores a uma data')
            print('[5] - Apagar e-mails de um mês/ano específico')
            print('[6] - Apagar e-mails de um ano específico')
            print('[7] - Apagar todos os e-mails')
            print('[0] - Sair')

            choice = input('Digite sua escolha (0-7): ').strip()

            if choice in ['0', '1', '2', '3', '4', '5', '6', '7']:
                return choice
            else:
                print(INVALID_OPTION_MSG)
        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return '0'
        except Exception as e:
            print(f'Erro ao ler entrada do usuário: {e}')


def get_year_from_user():
    while True:
        try:
            year_input = input('Digite o ano (ex: 2020): ').strip()
            year = int(year_input)

            if 1990 <= year <= 2030:
                return year
            else:
                print(INVALID_YEAR_MSG)
        except ValueError:
            print('Por favor, digite um ano válido (apenas números).')
        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return None
        except Exception as e:
            print(f'Erro ao ler ano: {e}')


def get_date_from_user():
    while True:
        try:
            date_input = input('Digite a data (DD/MM/AAAA): ').strip()
            from datetime import datetime
            datetime.strptime(date_input, '%d/%m/%Y')
            return date_input
        except ValueError:
            print(INVALID_DATE_FORMAT_MSG)
        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return None
        except Exception as e:
            print(f'Erro ao ler data: {e}')


def get_date_range_from_user():
    print('\nPara excluir e-mails entre duas datas:')
    start_date = get_date_from_user()
    if start_date is None:
        return None, None

    print('\nAgora, informe a data final:')
    end_date = get_date_from_user()
    if end_date is None:
        return None, None

    return start_date, end_date


def get_month_year_from_user():
    while True:
        try:
            month_input = input('Digite o mês (1-12): ').strip()
            month = int(month_input)
            if not 1 <= month <= 12:
                print(INVALID_MONTH_MSG)
                continue

            year = get_year_from_user()
            if year is None:
                return None, None

            return month, year
        except ValueError:
            print('Por favor, digite um mês válido (apenas números).')
        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return None, None
        except Exception as e:
            print(f'Erro ao ler mês/ano: {e}')
            return None, None


def display_welcome_message():
    print("=" * 22)
    print("     CLEAR E-MAIL")
    print("=" * 22)


def display_connection_message(imap_server):
    print(f"Conectando ao servidor IMAP: {imap_server}")


def display_result_message(deleted_count, year=None):
    if year:
        print(f'Total de {deleted_count} e-mails do ano {year} foram excluídos.')
    else:
        print(f'Total de {deleted_count} e-mails foram excluídos.')


def display_exit_message():
    print('Programa encerrado.')


def display_cancelled_message():
    print('Operação cancelada.')
