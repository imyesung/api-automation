FROM python:3.9-slim

WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 필요한 디렉토리 생성
RUN mkdir -p data/uploads data/downloads

# 실행
ENTRYPOINT ["python", "main.py"] 