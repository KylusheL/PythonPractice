# 1. 나의 초견
# 입력
s = input()
x = int(s[1])
y = ord(s[0]) - ord('a') + 1

moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

result = 0
for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    result += 1

print(result)

# 2. 책의 풀이
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 3. 얻어갈 점
'''
dx, dy를 따로 리스트로 두지 않고, 튜플화하여 하나의 리스트로 관리
'''
