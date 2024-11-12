import os
from src.clients.mobsf import MobSFClient
from src.core.validator import validate_apk_file
from src.config.settings import settings

class APKAnalyzer:
    def __init__(self):
        self.client = MobSFClient()
    
    def analyze(self, apk_filename: str) -> bool:
        """APK 파일 분석 실행"""
        # 파일 검증 (참조: src/main.py startLine: 9, endLine: 20)
        is_valid, result, file_size = validate_apk_file(apk_filename)
        if not is_valid:
            print(result)
            return False
            
        print(f"Analyzing {apk_filename} (size: {file_size} bytes)...")
        return self._process_analysis(result, apk_filename)
    
    def _process_analysis(self, apk_path: str, filename: str) -> bool:
        """분석 프로세스 실행"""
        # 파일 업로드 및 스캔 (참조: src/main.py startLine: 24, endLine: 34)
        upload_result = self.client.upload_file(apk_path)
        file_hash = upload_result.get('hash')
        
        if not file_hash:
            print("Error: Failed to upload APK")
            return False
        
        self.client.start_scan(file_hash)
        print("Scanning...")
        
        # 결과 저장 (참조: src/main.py startLine: 36, endLine: 48)
        self._save_reports(file_hash, filename)
        
        # 정리
        self.client.delete_scan(file_hash)
        return True
        
    def _save_reports(self, file_hash: str, filename: str):
        """분석 결과 저장"""
        report = self.client.get_report(file_hash)
        print("\nAnalysis Results:")
        print(report)
        
        pdf_report = self.client.download_report(file_hash, 'pdf')
        report_path = os.path.join(settings.DOWNLOAD_DIR, f"{filename}_report.pdf")
        
        with open(report_path, 'wb') as f:
            f.write(pdf_report)
            
        print(f"Analysis complete! Report saved to: {report_path}") 