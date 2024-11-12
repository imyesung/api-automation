import sys
from src.core.static import StaticAnalyzer
from src.utils.file_utils import ensure_directory
from src.config.settings import settings

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <apk_filename>")
        sys.exit(1)
    
    # 필요한 디렉토리 생성
    ensure_directory(settings.UPLOAD_DIR)
    ensure_directory(settings.DOWNLOAD_DIR)
    
    # APK 분석 실행
    analyzer = StaticAnalyzer()
    analyzer.analyze(sys.argv[1])

if __name__ == '__main__':
    main()