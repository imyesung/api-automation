import os
import sys
from mobsf_client import MobSFClient
from config import UPLOAD_DIR, DOWNLOAD_DIR

def analyze_apk(apk_filename):
    apk_path = os.path.join(UPLOAD_DIR, apk_filename)
    
    if not os.path.exists(apk_path):
        print(f"Error: {apk_filename} not found in uploads directory")
        return
        
    if not apk_path.lower().endswith('.apk'):
        print(f"Error: {apk_filename} is not an APK file")
        return
        
    file_size = os.path.getsize(apk_path)
    if file_size == 0:
        print(f"Error: {apk_filename} is empty")
        return
        
    print(f"Analyzing {apk_filename} (size: {file_size} bytes)...")
    
    client = MobSFClient()
    upload_result = client.upload_file(apk_path)
    file_hash = upload_result.get('hash')
    
    if not file_hash:
        print("Error: Failed to upload APK")
        return
    
    # Start scan
    scan_result = client.start_scan(file_hash)
    print("Scanning...")
    
    # Get JSON report
    report = client.get_report(file_hash)
    print("\nAnalysis Results:")
    print(report)
    
    # Save PDF report
    pdf_report = client.download_report(file_hash, 'pdf')
    report_path = os.path.join(DOWNLOAD_DIR, f"{apk_filename}_report.pdf")
    
    with open(report_path, 'wb') as f:
        f.write(pdf_report)
    
    print(f"Analysis complete! Report saved to: {report_path}")
    
    # Clean up
    client.delete_scan(file_hash)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <apk_filename>")
        sys.exit(1)
    
    analyze_apk(sys.argv[1])