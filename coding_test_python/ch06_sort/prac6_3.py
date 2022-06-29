# 동빈이는 두 개의 배열 A와 B를 가지고 있다.
# 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
# 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데,
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 한다.
# N, K, 그리고 배열 A와 B의 정보가 주어졌을 때,
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

n, k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort() # A는 오름차순 정렬
array_B.sort(reverse=True) # B는 내림차순 정렬

result = sum(array_A) # 최초의 A의 원소들의 합을 구한 뒤 원소를 교체할 때마다 갱신

for i in range(k):
    if array_A[i] >= array_B[i]: # A의 원소가 B의 원소보다 크거나 같으면 반복문을 탈출
        break
    result += array_B[i] - array_A[i] # 두 원소를 교체하면 합은 두 원소의 차 만큼 커짐
    
print(result)