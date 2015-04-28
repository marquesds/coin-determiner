def coinDeterminer(num):
    coins = [1, 5, 7, 9, 11]
    coins.sort()
    coins.reverse()
    cNum = 0
    if num in coins:
        cNum += 1
    else:
        while num > 0:
            for c in coins:
                if num % c == 0:
                    num -= c
                    cNum += 1
                    break
                elif num > c:
                    num -= c
                    cNum += 1
                    break

    return cNum


print(coinDeterminer(250))
