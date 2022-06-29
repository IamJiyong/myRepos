# 계수정렬
# 계수정렬의 시간 복잡도는 O(N + K)이다. (K는 데이터 중 최대값의 크기)
# 현존하는 정렬 알고리즘 중에서 기수 정렬(radix sort)과 더불어 가장 빠르다.

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에해당하는 인덱스의 값 증가

for i in range(len(count)): # 
    for j in range(count[i]):
        print(i,end=' ')