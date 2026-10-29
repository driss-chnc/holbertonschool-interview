#!/usr/bin/python3

def makeChange(coins, total):

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0

    for coin in coins:
        if total <= 0:
            break
        
        coins_count = total // coin
        total = total % coin

    if total != 0:
        return -1

    return coin_count