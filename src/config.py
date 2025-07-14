import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.imap_server = os.getenv('IMAP_SERVER', 'imap.gmail.com')

    def validate_credentials(self):
        if not self.email or not self.password:
            raise ValueError("As variáveis de ambiente EMAIL e PASSWORD devem ser definidas no arquivo .env.")

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_imap_server(self):
        return self.imap_server
