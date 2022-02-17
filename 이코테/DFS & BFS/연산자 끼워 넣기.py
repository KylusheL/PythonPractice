# 1. 나의 초견
n = int(input())
data = list(map(int, input().split()))
data.reverse()
operators = list(map(int, input().split()))

INF = 1e9
result = [-INF, INF]

def dfs(mid_result):
    if len(data) == 0:
        result[0] = max(result[0], mid_result)
        result[1] = min(result[1], mid_result)
        return
    operand = data.pop()
    if operators[0] > 0:
        operators[0] -= 1
        dfs(mid_result + operand)
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(mid_result - operand)
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        dfs(mid_result * operand)
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        dfs(int(mid_result / operand))
        operators[3] += 1
    data.append(operand)

first = data.pop()
dfs(first)
print(result[0])
print(result[1])

# 2. 책의 풀이
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)

# 3. 얻어갈 점
'''
DFS & BFS를 써야한다는 생각조차 못했다.
global 변수 사용법과 mutable 객체와 immutable 객체의 특징을 더 공부해야 한다.
https://livlikwav.github.io/python/python-mutable-and-namespace/#%EA%B2%B0%EB%A1%A0
또한, dfs 함수의 매개변수로 인덱스 값을 함께 넘겨주면, data를 스택마냥 pop append 할 필요가 없다.
'''
