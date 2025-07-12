# 📧 Clear Email

Um aplicativo Python para limpeza automática de e-mails via IMAP com interface interativa.

## 🌟 Funcionalidades

- ✅ **Exclusão por ano específico** - Remove e-mails de um ano determinado
- ✅ **Exclusão completa** - Remove todos os e-mails da caixa de entrada
- ✅ **Interface interativa** - Menu amigável com opções claras
- ✅ **Suporte a múltiplos provedores** - Gmail, Outlook, Yahoo e outros
- ✅ **Progresso em tempo real** - Acompanhe o processo de exclusão
- ✅ **Confirmação de segurança** - Evita exclusões acidentais
- ✅ **Estrutura modular** - Código organizado e profissional

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

| Provedor | Servidor IMAP | Porta |
|----------|---------------|-------|
| Gmail | imap.gmail.com | 993 |
| Outlook/Hotmail | outlook.office365.com | 993 |
| Yahoo | imap.mail.yahoo.com | 993 |
| AOL | imap.aol.com | 993 |

## 📖 Como usar

### Execução básica
```bash
python main.py
```

### Menu interativo
```
O que você deseja fazer?
[1] - Apagar e-mails de um ano específico
[2] - Apagar todos os e-mails
[0] - Sair
```

### Exemplo de uso
1. Execute o programa
2. Escolha a opção desejada
3. Para opção 1: Digite o ano (ex: 2020)
4. Para opção 2: Digite "SIM" para confirmar
5. Acompanhe o progresso da exclusão

## 🏗️ Estrutura do Projeto

```
clear-email/
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── .env                   # Variáveis de ambiente (não versionado)
├── README.md              # Este arquivo
├── LICENSE                # Licença MIT
└── src/
    ├── config.py          # Configurações e variáveis de ambiente
    ├── imap_connection.py # Conexões IMAP
    ├── email_operations.py # Operações com e-mails
    └── user_interface.py  # Interface do usuário
```

## 🔧 Módulos

### `config.py`
Gerencia configurações e variáveis de ambiente:
- Validação de credenciais
- Configuração padrão do servidor IMAP
- Classe `Config` para organizar settings

### `imap_connection.py`
Funções para conexão IMAP:
- `connect_imap()` - Conecta ao servidor
- `login_imap()` - Autentica usuário
- `logout_imap()` - Desconecta do servidor

### `email_operations.py`
Operações com e-mails:
- `fetch_emails()` - Busca todos os e-mails
- `delete_emails_by_year()` - Exclui e-mails por ano
- `delete_all_emails()` - Exclui todos os e-mails
- `show_remaining_emails()` - Mostra e-mails restantes

### `user_interface.py`
Interface do usuário:
- `get_user_choice()` - Menu de opções
- `get_year_from_user()` - Solicita ano
- Funções de exibição de mensagens

## ⚠️ Avisos Importantes

- **Backup seus e-mails** antes de usar o programa
- **Exclusões são permanentes** - não podem ser desfeitas
- **Use senhas de app** específicas, não sua senha principal
- **Teste primeiro** com uma conta secundária

## 🔒 Segurança

- Nunca compartilhe seu arquivo `.env`
- Use senhas de app específicas
- Mantenha suas credenciais seguras
- O arquivo `.env` está no `.gitignore`

## 🐛 Solução de Problemas

### Erro de autenticação
- Verifique se a verificação em duas etapas está habilitada
- Confirme se está usando a senha de app correta
- Teste as credenciais em um cliente de email

### Erro de conexão
- Verifique sua conexão com a internet
- Confirme o servidor IMAP correto
- Teste com diferentes provedores

### E-mails não encontrados
- Verifique se o ano está correto
- Confirme se há e-mails na caixa de entrada
- Teste com diferentes filtros

## 📝 Exemplo de Saída

```
==================================================
     LIMPADOR DE E-MAILS
==================================================
Conectando ao servidor IMAP: imap.gmail.com
Login realizado com sucesso!

O que você deseja fazer?
[1] - Apagar e-mails de um ano específico
[2] - Apagar todos os e-mails
[0] - Sair
Digite sua escolha (0, 1 ou 2): 1

Digite o ano (ex: 2020): 2020
100 de 1250 e-mails marcados para exclusão...
200 de 1250 e-mails marcados para exclusão...
...
1250 de 1250 e-mails marcados para exclusão...
Todos os e-mails foram apagados com sucesso!
Total de 1250 e-mails do ano 2020 foram excluídos.
Restam 15480 e-mails na caixa de entrada.
Logout realizado com sucesso.
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🆘 Suporte

Se você encontrar problemas ou tiver dúvidas:
1. Abra uma [issue](https://github.com/lucasrodriguescunha/clear-email/issues)
2. Descreva detalhadamente o problema encontrado

## 🔄 Changelog

### v.0.0.2
- ✅ Estrutura modular implementada
- ✅ Interface interativa aprimorada
- ✅ Exclusão por ano específico
- ✅ Melhor tratamento de erros
- ✅ Documentação completa

### v.0.0.1
- ✅ Versão inicial
- ✅ Exclusão básica de e-mails
- ✅ Suporte a Gmail

---

⚡ **Desenvolvido com Python** | 📧 **Para limpeza eficiente de e-mails** | 🔒 **Seguro e confiável**
