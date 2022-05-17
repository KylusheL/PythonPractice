# 1. 나의 초견
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

parent = [i for i in range(n)]
planet_x = sorted(planets, key = lambda x: x[0])
planet_y = sorted(planets, key = lambda x: x[1])
planet_z = sorted(planets, key = lambda x: x[2])
edges = []
for i in range(n - 1):
    xl, xr = planet_x[i], planet_x[i + 1]
    yl, yr = planet_y[i], planet_y[i + 1]
    zl, zr = planet_z[i], planet_z[i + 1]
    edges.append((xr[0] - xl[0], xl[3], xr[3]))
    edges.append((yr[1] - yl[1], yl[3], yr[3]))
    edges.append((zr[2] - zl[2], zl[3], zr[3]))
edges.sort()

cnt = 0
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        result += cost
        if cnt == n - 1:
            break
        
print(result)

# 2. 책의 풀이
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
 
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
# 노드의 개수 입력받기
n = int(input())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 3. 얻어갈 점
'''
좌표가 주어져있으므로 모든 edge를 돌지 않고, 후보군을 좁힌 뒤에 크루스칼 알고리즘 사용
메모리를 희생하는 과감함이 요구된다.
책에서는 x, y, z만 따로 저장했다.
필요한 데이터와 필요 없는 데이터를 구분하는 안목 필요
'''
