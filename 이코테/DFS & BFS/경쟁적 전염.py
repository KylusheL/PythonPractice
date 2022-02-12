# 1. 나의 초견
from collections import deque

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
compete = [[False] * n for _ in range(n)]
s, x, y = map(int, input().split())

t = 0
queue = deque()
for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            queue.append((i, j))
while t < s:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    now = queue.popleft()
    level = data[now[0]][now[1]]
    for move in zip(dx, dy):
        nx = now[0] + move[0]
        ny = now[1] + move[1]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        if data[nx][ny] == 0: # 첫 방문
            data[nx][ny] = level
            compete[nx][ny] = True
        elif compete[nx][ny] and data[nx][ny] > level: # 전염 우선순위
            data[nx][ny] = level
    if not queue:
        for i in range(n):
            for j in range(n):
                if compete[i][j]:
                    compete[i][j] = False
                    queue.append((i, j))
        if not queue:
            break
        t += 1
        
print(data[x - 1][y - 1])

# 2. 책의 풀이
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)
 
target_s, target_x, target_y = map(int, input().split())
 
# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

# 3. 얻어갈 점
'''
생략
'''
