import sys

input = sys.stdin.readline

N = int(input())

K = list(map(int, input().split()))

memozation = [0] * 100

memozation[0] = K[0]
memozation[1] = max(K[0], K[1])

for i in range(2,N):
    memozation[i] = max(memozation[i-1], memozation[i-2]+K[i])

print(memozation[N-1])