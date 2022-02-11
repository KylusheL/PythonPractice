# 1. 나의 초견
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True

while queue:
    v = queue.popleft()
    count = graph[v[0]][v[1]] + 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for pair in zip(dx, dy):
        nx = v[0] + pair[0]
        ny = v[1] + pair[1]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if graph[nx][ny] != 0:
            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = count
            elif graph[nx][ny] > count:
                graph[nx][ny] = count

print(graph[n - 1][m - 1])

# 2. 책의 풀이
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))

# 3. 얻어갈 점
'''
해결 전략을 미리 봐버렸다.
뱅 돌아가는 부분의 경우 어떻게 하나 싶었는데, 그래프 자체를 수정하면 된다.
또한, bfs이므로, 최단거리 여부를 확인할 필요가 없으며, visited도 별도로 저장할 필요가 없다.
(최초 방문 구분은 graph의 값이 1임을 통해 알 수 있기 때문)
'''
