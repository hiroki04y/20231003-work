from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    # 走行距離が0m以下の場合はNoneを返す
    if m <= 0:
        return None
    
    # 初乗り運賃の設定
    farst_fare = 610
    
    # 走行距離が1700m以下の場合は初乗り運賃を返す
    if m <= 1700:
        return farst_fare
    
    # 走行距離が1700mを超える場合は追加運賃を計算
    distance = m - 1700
    add_fare = (distance // 315) * 80
    
    # 初乗り運賃と追加運賃を合計して返す
    total = farst_fare + add_fare
    return total


    

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


