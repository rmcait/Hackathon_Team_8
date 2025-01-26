# Hackathon Project: Django Docker Environment

## 概要
このプロジェクトはハッカソン用に構築された Django を使用した開発環境です。Docker を使って簡単に開発環境をセットアップできます。

---

## **前提条件**
以下のツールがインストールされていることを確認してください:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## **セットアップ手順**

### 1. リポジトリをクローン
以下のコマンドを実行してリポジトリをクローンします:

```bash
git clone https://github.com/username/Hackathon_Team_8.git
cd Hackathon_Team_8

```
## 2. イメージのbuild
```
docker-compose build
```
## 3. コンテナの起動
```
docker-compose up -d
```
## 4. マイグレーションの適用
```
docker-compose exec web python manage.py migrate
```
## 5. スーパーユーザの作成
```
docker-compose exec web python manage.py createsuperuser
```
## 6. 開発サーバにアクセス
```
http://localhost:8005/
```


