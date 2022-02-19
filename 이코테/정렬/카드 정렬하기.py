# 1. 나의 초견
import heapq
n = int(input())
data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

result = 0
while len(data) >= 2:
    tmp = heapq.heappop(data)
    tmp += heapq.heappop(data)
    result += tmp
    heapq.heappush(data, tmp)

print(result)

# 2. 책의 풀이
import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)

# 3. 얻어갈 점
'''
알고리즘에서 한 번 잘못 생각하고,
시간초과에서 한 번 막혔다.
heapq에 익숙해질 필요가 있다.
'''
