for num in range(1, 101):
    string = ''

    # ここから記述

    #15の倍数ならFizzBuzz
    if num % 15 == 0:
        print('FizzBuzz')

    #3の倍数ならFizz
    elif num % 3 == 0:
        print('Fizz')

    #5の倍数ならBuzz
    elif num % 5 == 0:
        print('Buzz')

    #その他ならそのまま出力
    else:
        print(num)

    # ここまで記述

    print(string)

