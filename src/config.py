import os
from dotenv import load_dotenv

load_dotenv()

MOBSF_API_KEY = os.getenv('MOBSF_API_KEY')
MOBSF_PORT = os.getenv('MOBSF_PORT', '8000')
MOBSF_HOST = f"http://127.0.0.1:{MOBSF_PORT}"

# Debug 로그 제거
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'downloads')