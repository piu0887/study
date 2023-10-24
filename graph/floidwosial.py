import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
#2차원 거리테이블 리스트 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
#자신의 노드간의 거리는 0으로 변경
for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j :
            graph[i][j] = 0

#주어진 그래프 정보 입력
for _ in range(m):
    #a -> b 로 가는 비용은 c
    a, b, c = map(int,input().split())
    graph[a][b] = c

# k 를 거쳐가는 노드
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print ('도달할 수 없음', end='')
        else:
            print (graph[i][j],end='')
    print()