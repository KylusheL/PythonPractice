# 1. 나의 초견
def rotate(arr, size): # 시계방향으로 90도 회전하는 함수
    return [(y, size - 1 - x) for (x, y) in arr]

def solution(key, lock):
    n = len(lock)
    m = len(key)
    empty = [] # 자물쇠의 홈
    keyfill = [] # 열쇠의 돌기
    
    # 자물쇠의 홈
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                empty.append((i, j))
    # 홈이 하나도 없을 때 true
    if len(empty) == 0:
        return True
    
    # 열쇠의 돌기
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                keyfill.append((i, j))
    # 돌기가 홈보다 적을 때 false
    if len(keyfill) < len(empty):
        return False
    
    # 시간복잡도: O((N + M)^2)
    for _ in range(4): # 4방향으로 검증
        for i in range(-(m - 1), n): # key를 x축 방향으로 이동
            for j in range(-(m - 1), n): # key를 y축 방향으로 이동
                new_keyfill = [(x + i, y + j) for (x, y) in keyfill
                               if x + i >= 0 and x + i < n and y + j >= 0 and y + j < n ] # (i, j)만큼 이동 후 자물쇠 N * N 범위 내에 있는 돌기만 선택
                if new_keyfill == empty: # 홈과 돌기가 일치할 때
                    return True
        keyfill = sorted(rotate(keyfill, m)) # 돌기를 90도 회전
        
    # 모든 검증에 실패했을 때
    return False

# 2. 책의 풀이
# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

# 3. 얻어갈 점
'''
N이 작으면 완전탐색 생각해볼 것
matrix 90도 회전 함수 익숙해질 것
시간복잡도에 큰 차이가 없다면, 코드 라인 수를 줄이기보다는 코드를 구조화시켜 가독성을 높이는 것에 힘쓸 것
'''
