# The law of large numbers is the law of making the largest number by adding a given number M times when there is an array of various numbers.
# However, the number corresponding to a specific index of the array cannot be added more than K consecutively.
# It is also considered to be different even when the number corresponding to different indexes is the same.
# Output the result according to the law of large numbers given the size of the array N, the number of times the number is added M, and K.

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[N - 1]
second = arr[N - 2]

sum = 0

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