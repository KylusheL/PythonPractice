# 1. 나의 초견

# 입력
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

result = 0
for i in range(n):
    a[i].sort()
    min = a[i][0]
    result = min if min > result else result

print(result)

# 2. 책의 풀이

# 1) min 함수를 이용
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

# 2) 2중 반복문 구조를 이용
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

# 3. 얻어갈 점

'''
정렬 없이 min, max 함수를 통해 iterable 객체(리스트 등) 또는 여러 인자 중
최솟값, 최댓값을 찾는 것이 가능하다.
또한, 입력을 무작정 모두 저장할 필요 없이, 받을 때마다 처리할 수도 있다.
'''
