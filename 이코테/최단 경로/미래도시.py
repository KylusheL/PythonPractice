# 1. 나의 초견
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next in graph[now]:
            if dist[now] + 1 < dist[next]:
                dist[next] = dist[now] + 1
                heapq.heappush(q, (dist[next], next))

dijkstra(1)
if dist[k] == INF:
    result = -1
else:
    result += dist[k]

dist = [INF] * (n + 1)

dijkstra(k)
if dist[x] == INF or result == -1:
    result = -1
else:
    result += dist[x]

print(result)

# 2. 책의 풀이
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= 1e9:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
    
# 3. 얻어갈 점
'''
입력의 크기가 작으면 플로이드워셜을 구현하는 것이 편하다.
'''
