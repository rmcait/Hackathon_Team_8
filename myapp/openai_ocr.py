import openai
import os
import time
import base64
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()

# 環境変数から API キーを取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# APIキーが正しく読み込まれているか確認
if not OPENAI_API_KEY:
    raise ValueError("❌ エラー: OPENAI_API_KEY が環境変数に設定されていません！")

# OpenAI クライアントの初期化
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def analyze_image(image_path):
    """OpenAI API を使って画像を解析"""
    time.sleep(2)  # ✅ 2秒待機（API制限対策）

    # 画像を Base64 にエンコード
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    # OpenAI API にリクエストを送信
    response = client.chat.completions.create(
        model="gpt-4o",  # ✅ `gpt-4o` に変更
        messages=[
            {"role": "system", "content": "この画像の文章を教えて。"},
            {"role": "user", "content": [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}]},
        ],
    )

    return response.choices[0].message.content

# メイン処理
if __name__ == "__main__":
    # ✅ `static/openai/` 内の画像を使用
    image_path = "/app/static/openai/test2.png"
    print(f"使用する画像のパス: {image_path}")

    text = analyze_image(image_path)
    print("OCR 結果:", text)