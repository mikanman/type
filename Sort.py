import copy

def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)

    print(sortedArray)

    # 結果出力
    # [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    goal_list =[]

    def split_sort(sort_list, baise_item):

        #リストの要素数が1ならゴールのリストに追加
        if len(sort_list) <= 1:
            goal_list.append(baise_item)
            return 0
        
        #比較する右側のポイントと新しいリストの作成
        search_right_num = len(sort_list) - 1
        new_list = copy.copy(sort_list)

        #比較する左側のポイントをループで作成
        for search_left_num  in range(len(sort_list)):

            #比較する左側の値
            search_left = new_list[search_left_num]

            if search_left_num >= search_right_num:
                break #比較する左側の値が右側の値より大きいならbreak
            
            if search_left < baise_item:
                continue #比較する左側の値が基準の値より小さいならcontinue
            if search_left_num >= search_right_num:
                break #比較する左側の値が右側の値より大きいならbreak

            
            #比較する左側の値が右側の値より小さい間ループ
            while(search_left_num < search_right_num):

                #比較する右側の値
                search_right = new_list[search_right_num]

                #比較する右側の値が基準の値より小さいなら新しいリストに追加してbreak
                if search_right < baise_item:
                    new_list[search_left_num] = sort_list[search_right_num]
                    new_list[search_right_num] = sort_list[search_left_num]
                    search_right_num -= 1
                    break

                #比較する右側の値が基準の値より大きいなら右にずらす
                search_right_num -= 1

                if search_left_num == search_right_num:
                    break #比較する左側の値が右側の値より大きいならbreak
            
            if search_left_num == search_right_num:
                    break #比較する左側の値が右側の値より大きいならbreak
            


            
            
        if new_list[search_left_num] <= baise_item:
            left_list = new_list[:search_left_num+1]
        else:
            left_list = new_list[:search_left_num]
        
        if len(left_list) == 0:
            pass
        elif len(left_list) == 1:
            goal_list.append(left_list[0])
        else:
            split_sort(left_list, left_list[0])

        if new_list[search_right_num] >= baise_item:
            right_list = new_list[search_right_num:]
        else:
            right_list = new_list[search_right_num+1:]

        if len(right_list) == 0:
            pass
        elif len(right_list) <= 1:
            goal_list.append(right_list[0])
        else:
            split_sort(right_list, right_list[0])


    split_sort(array, pivot)

    return goal_list

    # ここまで記述

if __name__ == '__main__':
    main()