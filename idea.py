def ask_season():
    print("季節を選んでください：")
    print("1. 春")
    print("2. 夏")
    print("3. 秋")
    print("4. 冬")
    seasons = ["春", "夏", "秋", "冬"]
    choice = input("番号で選択: ")
    return seasons[int(choice)-1] if choice in "1234" else "春"

def ask_scene():
    print("場面を選んでください：")
    print("1. カジュアル")
    print("2. ビジネス")
    print("3. フォーマル")
    scenes = ["カジュアル", "ビジネス", "フォーマル"]
    choice = input("番号で選択: ")
    return scenes[int(choice)-1] if choice in "123" else "カジュアル"

def ask_color():
    color = input("入れてほしい色を入力してください（例：青、赤、白など）: ")
    return color if color else "白"

def suggest_outfits(season, scene, color):
    suggestions = []
    if scene == "カジュアル":
        if season == "春":
            suggestions = [
                f"{color}のパーカー＋デニム＋スニーカー",
                f"{color}のカーディガン＋チノパン＋ローファー",
                f"{color}のシャツ＋黒パンツ＋スニーカー"
            ]
        elif season == "夏":
            suggestions = [
                f"{color}のTシャツ＋ショートパンツ＋サンダル",
                f"{color}のポロシャツ＋薄手パンツ＋スニーカー",
                f"{color}の半袖シャツ＋ジーンズ＋スリッポン"
            ]
        elif season == "秋":
            suggestions = [
                f"{color}のニット＋カーゴパンツ＋ブーツ",
                f"{color}のパーカー＋デニム＋スニーカー",
                f"{color}の長袖シャツ＋ベスト＋チノパン"
            ]
        else:  # 冬
            suggestions = [
                f"{color}のコート＋セーター＋ジーンズ＋ブーツ",
                f"{color}のダウン＋パーカー＋黒パンツ＋スニーカー",
                f"{color}のニット＋厚手パンツ＋ブーツ"
            ]
    elif scene == "ビジネス":
        if season in ["春", "秋"]:
            suggestions = [
                f"{color}のジャケット＋白シャツ＋スラックス＋革靴",
                f"{color}のカーディガン＋シャツ＋グレーパンツ＋革靴",
                f"{color}のスーツ＋ネクタイ＋黒靴"
            ]
        elif season == "夏":
            suggestions = [
                f"{color}の半袖シャツ＋スラックス＋革靴",
                f"{color}のポロシャツ＋ベージュパンツ＋ローファー",
                f"{color}の薄手ジャケット＋白シャツ＋スラックス"
            ]
        else:  # 冬
            suggestions = [
                f"{color}のコート＋スーツ＋マフラー＋革靴",
                f"{color}のセーター＋シャツ＋スラックス＋ブーツ",
                f"{color}のダウン＋スーツ＋黒靴"
            ]
    else:  # フォーマル
        suggestions = [
            f"{color}のスーツ＋白シャツ＋ネクタイ＋革靴",
            f"{color}のドレス＋パンプス＋アクセサリー",
            f"{color}のジャケット＋ワンピース＋ヒール"
        ]
    return suggestions

def main():
    season = ask_season()
    scene = ask_scene()
    color = ask_color()
    print("\nおすすめのコーディネート：")
    outfits = suggest_outfits(season, scene, color)
    for i, outfit in enumerate(outfits, 1):
        print(f"{i}. {outfit}")

if __name__ == "__main__":
    main()