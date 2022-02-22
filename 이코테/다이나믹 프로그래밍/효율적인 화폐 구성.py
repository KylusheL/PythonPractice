# 1. 나의 초견
n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
INF = int(1e9)
d = [INF] * 10001

for coin in coins:
    d[coin] = 1

for i in range(1, m + 1):
    if d[i] == INF:
        for coin in coins:
            if i > coin:
                d[i] = min(d[i], d[i - coin] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])
    
# 2. 책의 풀이
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

# 3. 얻어갈 점
'''
dp 테이블을 필요한 만큼만 만들면 메모리에 좀 더 효율적
'''
