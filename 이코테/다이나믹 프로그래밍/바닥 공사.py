# 1. 나의 초견
n = int(input())

d = [0] * 1001
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])

# 2. 책의 풀이
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])

# 3. 얻어갈 점
'''
796796으로 나누는 위치에 주의할 것.
'''
