# 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다.
# 첫 번째 version의 코드는 O(M)의 시간 복잡도를 가진다.
# 아래와 같이 O(1)의 시간 복잡도를 갖도록 문제를 풀 수 있다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

in_a_row = first * k + second

result = in_a_row * (m // (k + 1)) + first * (m % (k + 1))

print(result)