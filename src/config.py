"""
Configuration module for email cleaner application
"""
import os

from dotenv import load_dotenv


class Config:
    """Configuration class to handle environment variables and settings"""

    def __init__(self):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.imap_server = os.getenv('IMAP_SERVER', 'imap.gmail.com')

    def validate_credentials(self):
        """Validate if required credentials are available"""
        if not self.email or not self.password:
            raise ValueError("As variáveis de ambiente EMAIL e PASSWORD devem ser definidas no arquivo .env.")

    def get_email(self):
        """Get email from environment variables"""
        return self.email

    def get_password(self):
        """Get password from environment variables"""
        return self.password

    def get_imap_server(self):
        """Get IMAP server from environment variables"""
        return self.imap_server
