# Clear Email

Este projeto é um script Python para apagar todos os e-mails de uma conta IMAP (Gmail, Outlook, etc.) de forma automatizada e segura.

## Requisitos
- Python 3.7+
- Conta de e-mail com acesso IMAP habilitado

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/lucasrodriguescunha/clear-email.git
   cd clear-email
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração
1. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```env
   EMAIL=seu_email@exemplo.com
   PASSWORD=sua_senha_ou_senha_de_app
   ```
   - Para Gmail, use uma senha de app (veja [documentação do Google](https://support.google.com/accounts/answer/185833)).
   - Exemplos de servidores IMAP:
     - Gmail: `imap.gmail.com`
     - Outlook: `imap-mail.outlook.com`
     - Yahoo: `imap.mail.yahoo.com`

2. **Nunca compartilhe seu arquivo `.env`!**

## Uso
Execute o script com:
```bash
python main.py
```
O script irá:
- Conectar ao servidor IMAP
- Listar a quantidade de e-mails encontrados
- Apagar todos os e-mails da caixa de entrada
- Exibir mensagens de progresso e possíveis erros

## Avisos Importantes
- **Todos os e-mails da caixa de entrada serão apagados!**
- Use com cautela. Não há como desfazer esta ação.
- Recomenda-se fazer backup dos e-mails antes de executar o script.

## Contribuição
Pull requests são bem-vindos. Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.

## Licença
[MIT](LICENSE)

