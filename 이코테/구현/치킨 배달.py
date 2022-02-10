# 1. 나의 초견
import itertools

def dist(house, shop):
    return abs(house[0] - shop[0]) + abs(house[1] - shop[1])

# 입력
n, m = map(int, input().split())
houses = []
shops = []
dists = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            houses.append((i + 1, j + 1))
        elif temp[j] == 2:
            shops.append((i + 1, j + 1))

answer = 0
m_shops = list(itertools.combinations(shops, m))
for shop_comb in m_shops:
    dist_total = 0
    for house in houses:
        dist_min = 0
        for shop in shop_comb:
            dist_curr = dist(house, shop)
            if dist_min == 0 or dist_curr < dist_min:
                dist_min = dist_curr
        dist_total += dist_min
    if answer == 0 or dist_total < answer:
        answer = dist_total

print(answer)

# 2. 책의 풀이
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

# 3. 얻어갈 점
'''
입력의 크기를 통해 과감하게 노가다 여부를 결정해야함.
함수 정의는 코드 중간에다 해도 됨.
최솟값을 구해야할 때 초기값으로 1e9 주는 것
'''
