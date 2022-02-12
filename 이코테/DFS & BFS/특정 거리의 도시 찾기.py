# 1. 나의 초견
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
dist = [-1] * (n + 1)

queue = deque()
queue.append(x)
dist[x] = 0
result = []

while queue: # 큐에 원소가 남아있을 때
    v = queue.popleft() # 첫 원소 pop
    for i in graph[v]:
        if dist[i] < 0: # 미방문 도시라면
            dist[i] = dist[v] + 1
            if dist[i] == k:
                result.append(i)
                continue
            queue.append(i)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for elem in result:
        print(elem)
        
# 2. 책의 풀이
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
    
# 3. 얻어갈 점
'''
백준에서 Python3으로는 시간초과가 떠서 PyPy3으로 제출해봐야 하는 경우가 종종 있음.
visited를 둘지, distance를 둘지 잘 결정한다.
반복문 종료조건 주의해서 작성할 것
문제에서 요구하는 출력(오름차순 등)에 맞는지 다시 한 번 점검할 것
'''
