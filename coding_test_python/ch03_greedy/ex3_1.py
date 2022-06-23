# You are a clerk who helps with the restaurant's bill.
# It is assumed that there are unlimited 500 won, 100 won, 50 won, and 10 won coins to be used as change at the counter.
# Find the minimum number of coins to be given back when the money for change is N won.
# However, N is always a multiple of 10.

N = int(input())

coins = [500, 100, 50, 10]
count_coins = 0

for coin in coins:
    count_coins += (N // coin)
    N = N % coin

print(count_coins)