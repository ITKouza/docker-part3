# ベースイメージの指定
FROM python:3.8

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルのコピー
COPY requirements.txt .

# 依存ライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルのコピー
COPY . .

# 環境変数の設定
ENV APP_PORT=5000

# コンテナ起動時に実行されるコマンド
CMD ["python", "app.py"]


