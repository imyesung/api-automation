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