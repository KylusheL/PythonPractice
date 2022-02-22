# 1. 나의 초견
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    data = []
    for i in range(0, len(temp), m):
        data.append(temp[i:i + m])
    
    for j in range(1, m):
        for i in range(n):
            prev_max = data[i][j - 1]
            if i > 0:
                prev_max = max(prev_max, data[i - 1][j - 1])
            if i < n - 1:
                prev_max = max(prev_max, data[i + 1][j - 1])
            data[i][j] += prev_max
    result = 0
    for i in range(n):
        result = max(result, data[i][m - 1])
    print(result)
    
# 2. 책의 풀이
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
    
# 3. 얻어갈 점
'''
전형적인 점화식 유형
'''
