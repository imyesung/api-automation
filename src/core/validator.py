import os
from src.config.settings import settings

def validate_apk_file(filename: str) -> tuple[bool, str, int]:
    """
    APK 파일 유효성 검사
    Returns:
        tuple: (is_valid, filepath, file_size)
    """
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    print(f"Looking for APK at: {filepath}")
    print(f"Directory exists: {os.path.exists(os.path.dirname(filepath))}")
    print(f"File exists: {os.path.exists(filepath)}")
    
    if not os.path.exists(filepath):
        return False, f"Error: {filename} not found in uploads directory", 0
        
    if not filepath.lower().endswith('.apk'):
        return False, f"Error: {filename} is not an APK file", 0
        
    file_size = os.path.getsize(filepath)
    if file_size == 0:
        return False, f"Error: {filename} is empty", 0
        
    return True, filepath, file_size 