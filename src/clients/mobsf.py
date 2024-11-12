import requests
import os
from src.config.settings import settings

class MobSFClient:
    def __init__(self):
        self.base_url = settings.MOBSF_HOST
        self.headers = {
            'X-Mobsf-Api-Key': settings.MOBSF_API_KEY
        }
    
    def upload_file(self, file_path):
        """Upload an APK file to MobSF"""
        upload_url = f"{self.base_url}/api/v1/upload"
        try:
            with open(file_path, 'rb') as f:
                filename = os.path.basename(file_path)
                files = {'file': (filename, f, 'application/vnd.android.package-archive')}
                response = requests.post(upload_url, files=files, headers=self.headers)
                print(f"Upload response status: {response.status_code}")
                print(f"Upload response content: {response.text}")
                response.raise_for_status()
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Upload error: {str(e)}")
            return {}

    def start_scan(self, file_hash):
        """Start scanning an uploaded file"""
        scan_url = f"{self.base_url}/api/v1/scan"
        data = {
            'hash': file_hash
        }
        response = requests.post(scan_url, data=data, headers=self.headers)
        return response.json()

    def get_report(self, file_hash):
        """Get scan report"""
        report_url = f"{self.base_url}/api/v1/report_json"
        data = {
            'hash': file_hash
        }
        response = requests.post(report_url, data=data, headers=self.headers)
        return response.json()

    def download_report(self, file_hash, report_type='json'):
        """Download scan report in JSON format"""
        report_url = f"{self.base_url}/api/v1/report_json"
        data = {
            'hash': file_hash
        }
        try:
            response = requests.post(report_url, data=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Download error: {str(e)}")
            return None

    def delete_scan(self, file_hash):
        """Delete a scan"""
        delete_url = f"{self.base_url}/api/v1/delete_scan"
        data = {
            'hash': file_hash
        }
        response = requests.post(delete_url, data=data, headers=self.headers)
        return response.json()

    def get_dynamic_apps(self):
        """동적 분석 가능한 앱 목록 조회"""
        url = f"{self.base_url}/api/v1/dynamic/get_apps"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"동적 분석 앱 목록 조회 실패: {str(e)}")
            return None

    def start_dynamic_analysis(self, file_hash: str, re_install: bool = True, install: bool = True):
        """동적 분석 시작"""
        url = f"{self.base_url}/api/v1/dynamic/start_analysis"
        data = {
            'hash': file_hash,
            're_install': 1 if re_install else 0,
            'install': 1 if install else 0
        }
        try:
            response = requests.post(url, data=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"동적 분석 시작 실패: {str(e)}")
            return None

    def get_logcat(self, package_name: str):
        """Get logcat logs"""
        url = f"{self.base_url}/api/v1/android/logcat"
        data = {'package': package_name}
        response = requests.post(url, data=data, headers=self.headers)
        return response.text