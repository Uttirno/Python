def countWays(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amount+1):
            ways[i] += ways[i - coin]

    return ways[amount]

coins = [1, 2, 5]
print(countWays(10, coins))