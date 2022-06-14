from collections import deque
import sys
input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(start):
    graph[start[0]][start[1]] = -1
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] > 0:
                graph[nx][ny] += 1
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1
                q.append((nx, ny))

def process(cheese):
    byebye = []
    result = []
    for x, y in cheese:
        if graph[x][y] >= 3:
            byebye.append((x, y))
        if graph[x][y] < 3:
            result.append((x, y))
    for bb in byebye:
        dfs(bb)
    return result
                    
    

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dfs((0, 0))

cheese = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if graph[i][j] > 0:
            cheese.append((i, j))

result = 0
while len(cheese) > 0:
    result += 1
    cheese = process(cheese)

print(result)

'''
은근 시간이 오래 걸린 문제
그래프를 언제 갱신할 지에 주의
'''
