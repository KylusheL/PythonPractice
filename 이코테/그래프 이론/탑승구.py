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

g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
cnt = 0
for _ in range(p):
    x = int(input())
    if find_parent(parent, x) > 0:
        union_parent(parent, x, parent[x] - 1)
        cnt += 1
    else:
        break
    print(parent[1:])

print(cnt)

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

# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)

# 3. 얻어갈 점
'''
서로소 집합 문제라는 것을 바로 캐치하지 못했고, 아이디어 구상에 시간이 오래 걸렸다.
또한, parent[x]와 find_parent(parent, x)는 다르다는 것을 명심할 것.
union 할 때 모든 parent가 업데이트되지 않는다.
'''
