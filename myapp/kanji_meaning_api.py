import requests

#Kanji Alive API使用
kanji_api_url = 'https://kanjialive-api.p.rapidapi.com/api/public/kanji/'
HEADERS = {
    "X-RapidAPI-Key": "0aa57fe4c6mshf87d96d94e24335p16d83ajsnb5d6a2a9f229",
    "X-RapidAPI-Host": "kanjialive-api.p.rapidapi.com"
}

def get_radical_image_url(radical_name):
    base_url = "https://raw.githubusercontent.com/kanjialive/kanji-data-media/master/radical-characters/"
    return base_url + radical_name + ".svg"


#漢字の情報をAPIから取得する
def get_kanji_info(kanji):
    res = requests.get(kanji_api_url + kanji, headers=HEADERS)

    if res.status_code == 200:
        data = res.json()
        if "kanji" in data:
            print(f"漢字: {data['kanji']['character']}")
            print(f"画数: {data['kanji']['strokes']['count']}画")
            print(f"音読み: {"".join(data['kanji']['onyomi']['katakana'])}")
            print(f"訓読み: {"".join(data['kanji']['kunyomi']['hiragana'])}")
            print(f"部首: {data['radical']['name']['hiragana']}")

            print(get_radical_image_url(data['radical']['name']["romaji"]))
           
            
           #例の二字熟語や名詞があれば表示
            if 'examples' in data:
                examples = data['examples'][:6]
                if examples:
                    print("例文:")
                    for example in examples:
                        print(f"・ {example['japanese']}")
                else:
                    print("例はないよ")
            else:
                pass

        else:
            print("ごめんね、この漢字のじょうほうが見つからないよ")
    else:
        print(f"エラーがおきたよ、しばらく時間をおいてね")




kanji = input("調べたい漢字を入力してください")
get_kanji_info(kanji)
