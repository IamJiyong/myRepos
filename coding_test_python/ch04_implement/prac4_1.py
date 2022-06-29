# 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

input_data = input()
j = int(input_data[1])
i = ord(input_data[0]) - ord('a') + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    if j + step[0] in range(1, 9) and i + step[1] in range(1, 9):
        result += 1

print(result)