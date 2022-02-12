# 1. 나의 초견
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

vacants = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            vacants.append((i, j))

result = 0
for candidate in combinations(vacants, 3):
    new_graph = copy.deepcopy(graph)
    for position in candidate:
        new_graph[position[0]][position[1]] = 1
    # 확산
    queue = deque()
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                queue.append((i, j))
                new_graph[i][j] = 3

                # bfs
                while queue:
                    dx = [-1, 1, 0, 0]
                    dy = [0, 0, -1, 1]
                    now = queue.popleft()
                    for move in zip(dx, dy):
                        nx = now[0] + move[0]
                        ny = now[1] + move[1]
                        if nx >= n or nx < 0 or ny >= m or ny < 0:
                            continue
                        if new_graph[nx][ny] == 0 or new_graph[nx][ny] == 2:
                            queue.append((nx, ny))
                            new_graph[nx][ny] = 3
    count = 0
    for i in range(n):
        count += new_graph[i].count(0)
    result = max(result, count)

print(result)

# 2. 책의 풀이
# BOJ에서는 [언어]를 PyPy3로 설정하여 제출해주세요.

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

# 3. 얻어갈 점
'''
n과 m이 작다는 점을 이용하여 완전탐색을 이용한다는 아이디어는 같으나 구현의 방식의 차이가 있음.
울타리의 개수를 늘렸다 줄여가며 재귀 함수를 이용한 dfs 아이디어를 눈여겨 봐둘 것
2차원 배열의 경우 deepcopy를 이용해서 복사해야 기존 배열에 영향을 주지 않음.
def 바깥에 있는 변수는 전역 변수이므로 인자로 넘겨주지 않아도 사용 가능
'''
