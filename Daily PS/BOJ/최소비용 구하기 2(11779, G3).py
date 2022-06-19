import copy
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = [0, [start]]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if distance[now][0] < d:
            continue
        for nxt, w in graph[now]:
            cost = d + w
            if distance[nxt][0] > cost:
                distance[nxt][0] = cost
                distance[nxt][1] = distance[now][1] + [nxt]
                heapq.heappush(q, (cost, nxt))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())
distance = [[INF, []] for _ in range(n + 1)]
dijkstra(start)

print(distance[end][0])
print(len(distance[end][1]))
print(*distance[end][1])

'''
다익스트라 + 경로까지 함께 출력하는 문제
답이 여러개 나올 수 있음.
'''
