import unittest
from src.clients.mobsf import MobSFClient

class TestDynamicAnalysis(unittest.TestCase):
    def setUp(self):
        self.client = MobSFClient()
    
    def test_get_dynamic_apps(self):
        """동적 분석 가능한 앱 목록 조회 테스트"""
        result = self.client.get_dynamic_apps()
        self.assertIsNotNone(result)
        self.assertIn('apks', result)
    
    def test_start_dynamic_analysis(self):
        """동적 분석 시작 테스트"""
        # 먼저 앱 목록을 가져옴
        apps = self.client.get_dynamic_apps()
        if not apps or not apps.get('apks'):
            self.skipTest("테스트할 수 있는 앱이 없습니다")
        
        # 첫 번째 앱으로 테스트
        test_app = apps['apks'][0]
        result = self.client.start_dynamic_analysis(test_app['MD5'])
        self.assertIsNotNone(result)
        self.assertIn('package', result)

if __name__ == '__main__':
    unittest.main() 