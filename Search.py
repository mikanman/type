def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    #探索の左側と右側の決定
    left = 0
    right = len(sorted_array) - 1

    #基準点がなくなるまで探索
    while(left <= right):

        #基準点を決める
        middle = (left + right) // 2

        #基準点と目的の値が同じなら位置を返す
        if(sorted_array[middle] == target_number):
            return middle

        #データを右半分にしぼり込む
        elif(sorted_array[middle] < target_number):
            left = middle + 1

        #データを左半分にしぼり込む
        else:
            right = middle - 1 

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()