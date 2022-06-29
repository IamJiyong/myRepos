# 하나의수열에는 다양한 수가 존재한다.
# 이러한 수는 크기에 상관없이 나열되어 있다.
# 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
# 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 계수 정렬 이용
count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1
    
for i in range(len(count) - 1, 0, -1):
    for j in range(count[i]):
        print(i, end=' ')
print()

# 기본 정렬 라이브러리 이용
array = sorted(array, reverse = True)

for i in array:
    print(i, end=' ')
print()