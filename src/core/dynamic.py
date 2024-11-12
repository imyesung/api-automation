import os
import json
from src.clients.mobsf import MobSFClient
from src.config.settings import settings

class DynamicAnalyzer:
    def __init__(self):
        self.client = MobSFClient()
    
    def analyze(self, file_hash: str, package_name: str) -> bool:
        """동적 분석 실행"""
        print("Starting dynamic analysis...")
        
        # 동적 분석 가능한 앱 목록 확인
        apps = self.client.get_dynamic_apps()
        if not self._verify_app_available(apps, file_hash):
            print("Error: App not available for dynamic analysis")
            return False
            
        # 동적 분석 시작
        result = self.client.start_dynamic_analysis(file_hash)
        if 'error' in result:
            print(f"Error starting analysis: {result['error']}")
            return False
            
        print(f"Dynamic analysis started for package: {package_name}")
        
        # 로그캣 모니터링 시작
        self._monitor_logcat(package_name)
        return True
        
    def _verify_app_available(self, apps: dict, target_hash: str) -> bool:
        """동적 분석 가능 여부 확인"""
        if 'apks' not in apps:
            return False
        return any(app['MD5'] == target_hash for app in apps['apks'])
        
    def _monitor_logcat(self, package_name: str):
        """로그캣 모니터링"""
        logs = self.client.get_logcat(package_name)
        log_path = os.path.join(settings.DOWNLOAD_DIR, f"{package_name}_logcat.txt")
        
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(logs)
            
        print(f"Logcat logs saved to: {log_path}")
