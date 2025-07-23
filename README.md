# 📧 Clear Email

Um aplicativo Python para limpeza automática de e-mails via IMAP com interface interativa.

## 🌟 Funcionalidades

- ✅ **Exclusão por data específica** - Remove e-mails de uma data determinada (ex: 25/12/2023)
- ✅ **Exclusão por período** - Remove e-mails entre duas datas específicas
- ✅ **Exclusão por antiguidade** - Remove e-mails anteriores a uma data específica
- ✅ **Exclusão por novidade** - Remove e-mails posteriores a uma data específica
- ✅ **Exclusão por mês/ano** - Remove e-mails de um mês específico em um ano
- ✅ **Exclusão por ano específico** - Remove e-mails de um ano determinado
- ✅ **Exclusão por palavras-chave** - Remove e-mails com palavras específicas no assunto (ex: "promoção", "newsletter", "spam")
- ✅ **Exclusão completa** - Remove todos os e-mails da caixa de entrada
- ✅ **Interface de usuário** - Menu amigável com opções 
- ✅ **Suporte a múltiplos provedores** - Gmail, Outlook, Yahoo e outros
- ✅ **Progresso em tempo real** - Acompanhe o processo de exclusão
- ✅ **Confirmação de segurança** - Evita exclusões acidentais
- ✅ **Estrutura modular** - Código modular e organizado

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/lucasrodriguescunha/clear-email.git
cd clear-email
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
EMAIL=seu-email@gmail.com
PASSWORD=sua-senha-de-app
```

## 🔧 Configuração

### Gmail
1. Habilite a **verificação em duas etapas**
2. Gere uma **senha de app** específica
3. Use a senha de app no arquivo `.env`

### Outros provedores de email

| Provedor        | Servidor IMAP         | 
|-----------------|-----------------------|
| Gmail           | imap.gmail.com        |
| Outlook/Hotmail | outlook.office365.com |
| Yahoo           | imap.mail.yahoo.com   |
| Apple iCloud    | imap.mail.me.com      |

## 📖 Como usar

Execute o programa:
```bash
python main.py
```

### Menu de opções:
```
[1] - Apagar e-mails de uma data específica
[2] - Apagar e-mails entre duas datas  
[3] - Apagar e-mails anteriores a uma data
[4] - Apagar e-mails posteriores a uma data
[5] - Apagar e-mails de um mês/ano específico
[6] - Apagar e-mails de um ano específico
[7] - Apagar e-mails por palavras-chave no assunto
[8] - Apagar todos os e-mails
[0] - Sair
```

### Exemplos de uso:

#### Exclusão por palavras-chave no assunto:
```
Opção: 7
Palavras-chave: promoção, newsletter, spam, oferta
```
- Remove todos os e-mails que contenham qualquer uma dessas palavras no assunto
- Permite adicionar mais palavras-chave durante o processo
- Busca é case-insensitive (não diferencia maiúsculas/minúsculas)

#### Exclusão por data específica:
```
Opção: 1
Data: 25/12/2023
```

#### Exclusão entre datas:
```
Opção: 2
Data inicial: 01/01/2023
Data final: 31/12/2023
```

## ⚙️ Estrutura do projeto

```
clear-email/
├── src/
│   ├── config.py           # Configurações e validações
│   ├── email_operations.py # Operações de e-mail
│   ├── imap_connection.py  # Conexão IMAP
│   └── user_interface.py   # Interface do usuário
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── .env                    # Variáveis de ambiente (criar)
└── README.md              # Este arquivo
```

## ⚠️ Avisos importantes

- **Sempre faça backup** dos seus e-mails importantes antes de usar
- **Teste primeiro** com uma conta de e-mail secundária
- As operações de exclusão são **irreversíveis**
- Use **senhas de app** específicas, nunca sua senha principal
- O programa exibe confirmações antes de executar exclusões

## 🛡️ Segurança

- Todas as credenciais são armazenadas localmente no arquivo `.env`
- Conexões IMAP são criptografadas
- Não há transmissão de dados para servidores externos
- Código-fonte aberto para auditoria

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🆘 Suporte

Se você encontrar problemas ou tiver dúvidas:
1. Abra uma [issue](https://github.com/lucasrodriguescunha/clear-email/issues)
2. Descreva detalhadamente o problema encontrado

---

⚡ **Desenvolvido com Python** | 📧 **Para limpeza eficiente de e-mails** | 🔒 **Seguro e confiável**
