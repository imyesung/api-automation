import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        
        self.MOBSF_API_KEY = os.getenv('MOBSF_API_KEY')
        self.MOBSF_PORT = os.getenv('MOBSF_PORT', '8000')
        self.MOBSF_HOST = f"http://127.0.0.1:{self.MOBSF_PORT}"
        
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.UPLOAD_DIR = os.path.join(self.BASE_DIR, 'data', 'uploads')
        self.DOWNLOAD_DIR = os.path.join(self.BASE_DIR, 'data', 'downloads')

settings = Settings()