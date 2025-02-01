import json
import re

#テキストから漢字を抽出してリストとして返す,[一-龥]はUnicodeの漢字↓
def text_to_kanjii(text):
    return re.findall(r'[一-龥]',text)


#抽出された漢字のリストを学年別に分類
def classify_kanji_by_grade(kanji_list):
    classified_kanji = {grade: set() for grade in Grade_kanji_dict.keys()}
    #リストにない漢字用
    classified_kanji["unknown"] = set()


   #kanji_list内の漢字を1つずつ学年別リストに照合する
    for kanji in kanji_list:
        found = False
        for grade, kanji_set in Grade_kanji_dict.items():
            if kanji in kanji_set:
                classified_kanji[grade].add(kanji)
                found = True
                break

        if not found:
                classified_kanji["unknown"].add(kanji)
  #重複を防ぐためにsetにしていたのをlistに戻す
    return {grade: list(kanji_set) for grade, kanji_set in classified_kanji.items()}



#学年ごとの漢字データ
Grade_kanji_dict = {
  1:"一右雨円王音下火花貝学気九休玉金空月犬見五口校左三山子四糸字耳七車手十出女小上森人水正生青夕石赤千川先早草足村大男竹中虫"
    "町天田土二日入年白八百文木本名目立力林六",

  2:"引羽雲園遠何科夏家歌画回会海絵外角楽活間丸岩顔汽記帰弓牛魚京強教近兄形計元言原戸古午後語工公広交光考行高黄合谷国黒今才細"
    "作算止市矢姉思紙寺自時室社弱首秋週春書少場色食心新親図数西声星晴切雪船線前組走多太体台地池知茶昼長鳥朝直通弟店点電刀冬当"
    "東答頭同道読内南肉馬売買麦半番父風分聞米歩母方北毎妹万明鳴毛門夜野友用曜来里理話",

  3:"悪安暗医委意育員院飲運泳駅央横屋温化荷界開階寒感漢館岸起期客究急級宮球去橋業曲局銀区苦具君係軽血決研県庫湖向幸港号根祭皿"
    "仕死使始指歯詩次事持式実写者主守取酒受州拾終習集住重宿所暑助昭消商章勝乗植申身神真深進世整昔全相送想息速族他打対待代第題"
    "炭短談着注柱丁帳調追定庭笛鉄転都度投豆島湯登等動童農波配倍箱畑発反坂板皮悲美鼻筆氷表秒病品負部服福物平返勉放味命面問役薬"
    "由油有遊予羊洋葉陽様落流旅両緑礼列練路和",

  4:"愛案以衣位囲胃印英栄塩億加果貨課芽改械害街各覚完官管関観願希季紀喜旗器機議求泣救給挙漁共協鏡競極訓軍郡径型景芸欠結建健験"
    "固功好候航康告差菜最材昨札刷殺察参産散残士氏史司試児治辞失借種周祝順初松笑唱焼象照賞臣信成省清静席積折節説浅戦選然争倉巣"
    "束側続卒孫帯隊達単置仲貯兆腸低底停的典伝徒努灯堂働特得毒熱念敗梅博飯飛費必票標不夫付府副粉兵別辺変便包法望牧末満未脈民無"
    "約勇要養浴利陸良料量輪類令冷例歴連老労録",

  5:"圧移因永営衛易益液演応往桜恩可仮価河過賀快解格確額刊幹慣眼基寄規技義逆久旧居許境均禁句群経潔件券険検限現減故個護効厚耕鉱"
    "構興講混査再災妻採際在財罪雑酸賛支志枝師資飼示似識質舎謝授修述術準序招承証条状常情織職制性政勢精製税責績接設舌絶銭祖素総"
    "造像増則測属率損退貸態団断築張提程適敵統銅導徳独任燃能破犯判版比肥非備俵評貧布婦富武復複仏編弁保墓報豊防貿暴務夢迷綿輸余預容略留領",

  6:"異遺域宇映延沿我灰拡革閣割株干巻看簡危机揮貴疑吸供胸郷勤筋系敬警劇激穴絹権憲源厳己呼誤后孝皇紅降鋼刻穀骨困砂座済裁策冊蚕"
    "至私姿視詞誌磁射捨尺若樹収宗就衆従縦縮熟純処署諸除将傷障城蒸針仁垂推寸盛聖誠宣専泉洗染善奏窓創装層操蔵臓存尊宅担探誕段暖"
    "値宙忠著庁頂潮賃痛展討党糖届難乳認納脳派拝背肺俳班晩否批秘腹奮並陛閉片補暮宝訪亡忘棒枚幕密盟模訳郵優幼欲翌乱卵覧裏律臨朗論"
}


"""
text="Unicode（ユニコード）とは、世界中の言語や記号に番号を割り当てて定義した文字コードの規格です。"
kanji_list = text_to_kanji(text)
classified_result = classify_kanji_by_grade(kanji_list)
print("抽出された漢字:", kanji_list)
print("分類結果:", json.dumps(classified_result, ensure_ascii=False))
"""