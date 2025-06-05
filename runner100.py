import random

# ダミーの選手名リスト（日本人・外国人混合）
names = [
"山田 太郎", "佐藤 健", "鈴木 一郎", "田中 直樹", "高橋 亮", "伊藤 翔", "渡辺 剛", "中村 優", "小林 大輔", "加藤 健太",
"吉田 拓海", "山本 直人", "松本 俊介", "斎藤 祐樹", "清水 健", "林 優太", "森本 大地", "池田 亮介", "橋本 直樹", "阿部 慎之助",    "Alex Johnson", "Michael Smith", "John Williams", "David Brown", "Chris Miller", "James Wilson", "Robert Moore", "Daniel Taylor", "Matthew Anderson", "Joshua Thomas",
    "Kevin Lee", "Brian Harris", "Jason Clark", "Ryan Lewis", "Eric Walker", "Andrew Hall", "Justin Young", "Brandon King", "Athony Wright", "Steven Scott",
    "Benjamin Green", "Samuel Adams", "Jacob Baker", "Logan Nelson", "Jack Carter", "Luke Mitchell", "Mason Perez", "Ethan Roberts", "Noah Turner", "Liam Phillips"
]

# 身長（cm）と体重（kg）の範囲
HEIGHT_MIN, HEIGHT_MAX = 165, 200
WEIGHT_MIN, WEIGHT_MAX = 60, 95

# タイム（秒）の範囲
TIME_MIN, TIME_MAX = 9.56, 12.99

# 選手データ生成
runners = []
for name in names:
    height = round(random.uniform(HEIGHT_MIN, HEIGHT_MAX), 1)
    weight = round(random.uniform(WEIGHT_MIN, WEIGHT_MAX), 1)
    time = round(random.uniform(TIME_MIN, TIME_MAX), 2)
    runners.append({
        "name": name,
        "height": height,
        "weight": weight,
        "time": time
    })

# タイムが良い順（昇順）にソート
runners_sorted = sorted(runners, key=lambda x: x["time"])

# 結果表示
print(f"{'順位':<4} {'名前':<15} {'タイム(s)':<8} {'身長(cm)':<9} {'体重(kg)':<9}")
for i, runner in enumerate(runners_sorted, 1):
    print(f"{i:<4} {runner['name']:<15} {runner['time']:<8} {runner['height']:<9} {runner['weight']:<9}")