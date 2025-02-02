import openai
import os
import base64
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .text_to_kanji import text_to_kanjii
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
    
# Create your views here.
def indexfunc(request):
    return render(request, 'index.html')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # `manage.py` のあるディレクトリ
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "openai")  # `static/openai/` フォルダ

def upload_image(request):
    """画像アップロードとOCR処理"""
    if request.method == "POST":
        if "image" not in request.FILES:
            return JsonResponse({"error": "画像がアップロードされていません"}, status=400)

        file = request.FILES["image"]
        file_name = file.name  # 元のファイル名
        file_path = os.path.join(UPLOAD_DIR, file_name)  # 保存先パス

        # 📌 `static/openai/` ディレクトリがなければ作成
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # 画像を `static/openai/` に保存
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        # OCRを実行
        text = analyze_image(file_path)

        # フロントエンドでアクセスできるパスを返す
        image_url = f"/static/openai/{file_name}"

        return JsonResponse({"text": text, "image_url": image_url})

    return render(request, "upload.html")


def process_image(request):
    """画像を処理してOCR結果ページへリダイレクト"""
    if request.method == "POST":
        if "image" not in request.FILES:
            return JsonResponse({"error": "画像がアップロードされていません"}, status=400)

        file = request.FILES["image"]
        file_name = default_storage.save(f"uploads/{file.name}", ContentFile(file.read()))
        file_path = os.path.join("media", file_name)

        # OCRを実行
        ocr_text = analyze_image(file_path)
        
        text_to_kanji = text_to_kanjii(ocr_text)
        
        

        # OCR結果を `result.html` に渡す
        return render(request, "result.html", {"ocr_text": text_to_kanji, "image_url": f"/media/uploads/{file.name}"})

    return redirect("upload_image")