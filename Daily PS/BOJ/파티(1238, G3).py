import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for nxt, w in graph[now]:
            cost = d + w
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return distance[end]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int,input().split())
    graph[a].append((b, w))

result = 0
for i in range(1, n + 1):
    result = max(result, dijkstra(i, x) + dijkstra(x, i))

print(result)

'''
전형적인 다익스트라
'''
