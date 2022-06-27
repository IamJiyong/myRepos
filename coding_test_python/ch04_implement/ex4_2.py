# 정수N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

# 시간 제한이 2초이므로 3중 반복문을 이용해 계산하더라도 문제를 해결할 수 있다.

n = int(input())

result = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)