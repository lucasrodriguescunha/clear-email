OPERATION_CANCELLED_MSG = '\nOperação cancelada pelo usuário.'
INVALID_YEAR_MSG = 'Ano inválido! Por favor, digite um ano entre 1990 e 2030.'
INVALID_MONTH_MSG = 'Mês inválido! Digite um número entre 1 e 12.'
INVALID_DATE_FORMAT_MSG = 'Data inválida! Use o formato DD/MM/AAAA (exemplo: 25/12/2023)'
INVALID_OPTION_MSG = 'Opção inválida! Por favor, digite um número entre 0 e 8.'


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
            print('[7] - Apagar e-mails por palavras-chave no assunto')
            print('[8] - Apagar todos os e-mails')
            print('[0] - Sair')

            choice = input('Digite sua escolha (0-8): ').strip()

            if choice in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
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


def get_keywords_from_user():
    while True:
        try:
            print('\nDigite as palavras-chave que deseja buscar no assunto dos e-mails.')
            print('Exemplos: promoção, newsletter, spam, oferta')
            print('Você pode digitar várias palavras separadas por vírgula.')

            keywords_input = input('Palavras-chave: ').strip()

            if not keywords_input:
                print('Por favor, digite pelo menos uma palavra-chave.')
                continue

            # Dividir por vírgula e limpar espaços em branco
            keywords = [keyword.strip() for keyword in keywords_input.split(',') if keyword.strip()]

            if not keywords:
                print('Por favor, digite pelo menos uma palavra-chave válida.')
                continue

            # Mostrar as palavras-chave para confirmação
            print(f'\nPalavras-chave que serão usadas na busca: {", ".join(keywords)}')
            confirm = input('Confirma essas palavras-chave? (s/n): ').strip().lower()

            if confirm in ['s', 'sim', 'y', 'yes']:
                return keywords
            elif confirm in ['n', 'não', 'nao', 'no']:
                continue
            else:
                print('Por favor, responda com "s" para sim ou "n" para não.')

        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return None
        except Exception as e:
            print(f'Erro ao ler palavras-chave: {e}')


def add_more_keywords(existing_keywords):
    while True:
        try:
            print(f'\nPalavras-chave atuais: {", ".join(existing_keywords)}')
            print('Deseja adicionar mais palavras-chave? (s/n)')

            choice = input('Resposta: ').strip().lower()

            if choice in ['n', 'não', 'nao', 'no']:
                return existing_keywords
            elif choice in ['s', 'sim', 'y', 'yes']:
                existing_keywords = _process_new_keywords(existing_keywords)
            else:
                print('Por favor, responda com "s" para sim ou "n" para não.')

        except KeyboardInterrupt:
            print(OPERATION_CANCELLED_MSG)
            return existing_keywords
        except Exception as e:
            print(f'Erro ao adicionar palavras-chave: {e}')
            return existing_keywords

def _process_new_keywords(existing_keywords):
    new_keywords_input = input('Digite as novas palavras-chave (separadas por vírgula): ').strip()

    if not new_keywords_input:
        print('Nenhuma palavra-chave válida foi digitada.')
        return existing_keywords

    new_keywords = [keyword.strip() for keyword in new_keywords_input.split(',') if keyword.strip()]

    # Adicionar apenas palavras-chave que não existem ainda
    for keyword in new_keywords:
        if keyword.lower() not in [k.lower() for k in existing_keywords]:
            existing_keywords.append(keyword)

    print(f'Palavras-chave atualizadas: {", ".join(existing_keywords)}')
    return existing_keywords
