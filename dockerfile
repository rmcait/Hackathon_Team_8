# Pythonの公式イメージを使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトファイルをコピー
COPY . /app/

# 開発サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]