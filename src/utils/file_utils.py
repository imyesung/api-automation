import os
import shutil
from typing import Optional

def ensure_directory(directory: str) -> None:
    """디렉토리가 없으면 생성"""
    os.makedirs(directory, exist_ok=True)

def get_file_size(filepath: str) -> Optional[int]:
    """파일 크기 반환"""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return None

def clean_directory(directory: str) -> None:
    """디렉토리 내용 정리"""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            os.unlink(filepath) 