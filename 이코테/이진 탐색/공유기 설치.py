# 1. 나의 초견
from bisect import bisect_left

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()

def plantable(step):
    pos = array[0]
    count = 1
    while count < c:
        next_idx = bisect_left(array, pos + step)
        if next_idx == n:
            return False
        pos = array[next_idx]
        count += 1
    return True

result = 0
start = 1
end = (array[-1] - array[0]) // (c - 1)
while start <= end:
    mid = (start + end) // 2
    if plantable(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

# 2. 책의 풀이
# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
     array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치하기
    for i in range(1, n): # 앞에서부터 차근차근 설치 
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)

# 3. 얻어갈 점
'''
이분 탐색 아이디어가 떠오르지 않아 질문 검색을 통해 힌트를 보았다.
파라메트릭 서치에 익숙해져야 한다.
https://sarah950716.tistory.com/16
책의 코드는 설치 가능 여부 확인의 시간복잡도가 O(N)이지만
이 또한 이분탐색을 이용하면 O(log N)에 해결 가능
max gap도 c - 1로 나눠두면 탐색 범위가 줄어든다.
'''
