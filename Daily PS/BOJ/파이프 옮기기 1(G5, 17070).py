import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
q = []
heapq.heappush(q, ((0, 1), 0))
while q:
    now, state = heapq.heappop(q)
    x, y = now
    print(now, state, dp[x][y][state])
    if state < 2 and y + 1 < n:
        nx, ny = x, y + 1
        if graph[nx][ny] == 0:
            if dp[nx][ny][0] == 0:
                heapq.heappush(q, ((nx, ny), 0))
            dp[nx][ny][0] += dp[x][y][state]
    if x + 1 < n and y + 1 < n:
        nx, ny = x + 1, y + 1
        if graph[x][ny] == 0 and graph[nx][y] == 0 and graph[nx][ny] == 0:
            if dp[nx][ny][1] == 0:
                heapq.heappush(q, ((nx, ny), 1))
            dp[nx][ny][1] += dp[x][y][state]
    if state > 0 and x + 1 < n:
        nx, ny = x + 1, y
        if graph[nx][ny] == 0:
            if dp[nx][ny][2] == 0:
                heapq.heappush(q, ((nx, ny), 2))
            dp[nx][ny][2] += dp[x][y][state]
print(sum(dp[-1][-1]))

'''
bottom-up dp에서는 순서가 차곡차곡 쌓이도록 할 것
'''
