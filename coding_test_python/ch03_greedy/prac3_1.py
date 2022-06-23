# '큰 수의 법칙'은 다양한 수로 이루어진 배열이 있을 대 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 리스트를 정렬한다.(오름차순이 default)
arr.sort()
first = arr[N - 1]
second = arr[N - 2]

sum = 0

# 루프를 돌며 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복한다.
while True:
    for i in range(K):
        if M == 0:
            break
        sum += first
        M -= 1
    
    if M == 0:
        break

    sum += second
    M -= 1

print(sum)

# 첫 번째 version의 코드는 O(M)의 시간 복잡도를 가진다.
# 계산을 통해 아래와 같이 O(1)의 시간 복잡도를 갖도록 문제를 풀 수 있다.

first = arr[N - 1]
second = arr[N - 2]

in_a_row = first * K + second

result = in_a_row * (M // (K + 1)) + first * (M % (K + 1))

print(result)