# 1. 나의 초견
# 입력
n = int(input())
plan = input().split()
x, y = 1, 1
for way in plan:
    if way == 'L':
        y = y - 1 if y > 1 else y
    elif way == 'R':
        y = y + 1 if y < n else y
    elif way == 'U':
        x = x - 1 if x > 1 else x
    elif way == 'D':
        x = x + 1 if x < n else x

print(x, y)

# 2. 책의 풀이
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

# 3. 얻어갈 점
'''
상하좌우 이동 관련 문제에서 dx, dy 배열을 이용할 것
x, y의 새 좌표인 new x, new y를 nx, ny로 표현하는 것
'''
