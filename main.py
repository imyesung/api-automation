import sys
from src.utils.file_utils import ensure_directory
from src.core.static import StaticAnalyzer
from src.config.settings import settings

def main(apk_filename: str):
    # 필요한 디렉토리 생성
    ensure_directory(settings.UPLOAD_DIR)
    ensure_directory(settings.DOWNLOAD_DIR)
    
    # 정적 분석 실행
    static_analyzer = StaticAnalyzer()
    static_analyzer.analyze(apk_filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <apk_filename>")
        sys.exit(1)
    
    main(sys.argv[1])