import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra (start) :
    que = []
    heapq.heappush(que, (0, start)) # 시작 노드 정보 우선순위 큐에 삽입
    distance[start] = 0
    while que:
        dist, node = heapq.heappop(que)
        #큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 (=방문한 셈) 무시
        if distance[node] < dist:
            continue
        #큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1] # 시작->노드거리 + node ->node 의 인접 노드 거리
            if cost < distance[next[0]] :   # cost < 시작 -> node의 인접노드 거리
                    distance[next[0]] = cost
                    heapq.heappush(que,(cost, next[0])) # 우선순위큐에 업데이트

dijkstra(start)

for i in range(1, len(distance)) :
    if distance[i] == INF:
          print('도달할수 없음')
    else:
         print(distance[i])