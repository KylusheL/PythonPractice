# 1. 나의 초견
# 입력
n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()

result = 0
for ball in balls:
    result += n - balls.count(ball)

print(result // 2)

# 2. 책의 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)

# 3. 얻어갈 점
'''
시간복잡도에서 크게 차이가 난다. 나의 풀이는 정렬에서 O(NlogN), 순회 + count함수에서 O(N^2)
책의 풀이는 O(N)이다.
먼저, M의 범위가 10 이하로 제한되어 있다는 점에 주목해야 시간복잡도를 줄이는 전략을 구상 가능.
루프를 두 번 돌더라도 개수를 기록해두면, 시간 복잡도가 O(N)에서 그친다.
'''
