# Flask サンプルアプリ Dockerパート４

このアプリは Python 3.8 で動作するシンプルな Flask アプリケーションです。
アプリには単一のルート "/ " が含まれています。
Dockerビルドを紹介するためのシンプルなアプリ


## Docker コンテナで実行する
Docker を使用してアプリケーションを実行するには、以下の手順を実行します。

Docker をインストールしていない場合は、Docker 公式ウェブサイト からインストールしてください。

## Docker イメージをビルドします:
-t オプション: イメージにタグを付けます。
```
docker build -t flask-sample .
```
## Docker コンテナの起動:
```
docker run -p 5000:5000 flask-sample
```
-p オプション: ポートのマッピング。左側がホストのポート、右側がコンテナのポートです。
flask-sample: ビルドした Docker イメージの名前。
アプリケーションが http://localhost:5000 で実行されます。
