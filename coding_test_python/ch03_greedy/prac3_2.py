# Number card game is a game in which one card with the highest number is drawn from among several number cards.
# However, you must draw cards while observing the rules of the game, and the rules are as follows.
# 1. Numbered cards are placed in the shape of N x M.
#    In this case, N means the number of rows and M means the number of columns.
# 2. First, select the row containing the card you want to draw.
# 3. Then, you must draw the lowest numbered card among the cards in the selected row.
# 4. Therefore, when selecting a row from which to draw cards at the beginning, you should plan a strategy so that you can draw the highest number of cards in the end, considering that the lowest card will be drawn from that row later.
# Create a program that draws cards according to the rules of the game when the cards are placed in the shape of N x M.

n, m = map(int, input().split())
min_cards = []

# 한 줄 씩 입력 받고, 그 줄에서 가장 작은 수들을 리스트에 모아놓는다.
for i in range(n):
    cards = list(map(int, input().split()))
    min_cards.append(min(cards))

# 각 행에서 가장 작은 수들 중 가장 큰 수를 구한다.
result = max(min_cards)

print(result)