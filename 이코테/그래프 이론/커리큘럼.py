from collections import deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for elem in info[1:-1]:
        indegree[i] += 1
        graph[elem].append(i)

def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for elem in result[1:]:
        print(elem)

topology_sort()

# 얻어갈 점
'''
혼자서 작성하다가 꼬여서 풀이를 봄
max 사용부분에서 헷갈렸다.
위상정렬 코드 좀 더 연습 필요
'''
