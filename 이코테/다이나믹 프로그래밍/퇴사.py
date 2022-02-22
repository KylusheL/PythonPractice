# 1. 나의 초견
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)


for i in range(1, n + 1):
    for j in range(i - 5, i):
        if j >= 0:
            if j + data[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + data[j][1])
            else:
                dp[i] = max(dp[i], dp[j])

print(dp[n])

# 2. 책의 풀이
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)

# 3. 얻어갈 점
'''
사이드 케이스 (중간에 max value가 생기지만, 상담을 진행하지 않는 경우)를 고려하지 못하였음.
'''
