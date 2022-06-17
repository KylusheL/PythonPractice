import copy
import sys
input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def spread(graph):
    new_graph = copy.deepcopy(graph)
    global n, m
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                part = graph[x][y] // 5
                if part < 1:
                    continue
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if nx >= n or nx < 0 or ny >= m or ny < 0:
                        continue
                    if graph[nx][ny] == -1:
                        continue
                    new_graph[nx][ny] += part
                    new_graph[x][y] -= part
    return new_graph

def clean(idx):
    global n, m
    for i in range(idx - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for i in range(m - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(idx):
        graph[i][-1] = graph[i + 1][-1]
    for i in range(m - 1, 0, -1):
        graph[idx][i] = graph[idx][i - 1]
    graph[idx][1] = 0
    for i in range(idx + 2, n - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(m - 1):
        graph[-1][i] = graph[-1][i + 1]
    for i in range(n - 1, idx + 1, -1):
        graph[i][-1] = graph[i - 1][-1]
    for i in range(m - 1, 0, -1):
        graph[idx + 1][i] = graph[idx + 1][i - 1]
    graph[idx + 1][1] = 0

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cleaner = 0
for i in range(n):
    if graph[i][0] == -1:
        cleaner = i
        break
for a in range(t):
    graph = spread(graph)
    clean(cleaner)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)

'''
너무나 빡구현 문제인 것
deepcopy가 시간을 많이 잡아먹어서 PyPy3로 제출해서 통과함
'''
