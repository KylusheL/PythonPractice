# 1. 나의 초견
n = int(input())
data = list(map(int, input().split()))

d = [0] * 101
d[1] = data[0]
d[2] = max(data[0], data[1])

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + data[i - 1])

print(d[n])

# 2. 책의 풀이
# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])

# 3. 얻어갈 점
'''
인덱스에 주의할 것
초기조건 확실히 할 것(이번에 max 빼먹었음)
'''
