# 1. 나의 초견

# N, M, K
# N개의 자연수
# M: 더하는 횟수, K: 같은 인덱스의 원소가 연속해서 더해질 수 있는 횟수
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

acc = 1
result = 0
for _ in range(M):
    if acc == 0:
        result += arr[-2]
    else:
        result += arr[-1]
    acc = (acc + 1) % K

print(result)

# 2. 책의 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)

# 3. 얻어갈 점

'''
반복되는 수열을 파악하여 수학적으로 접근, for 문을 쓰지 않아 시간 절약
가장 큰 수와 두 번째로 큰 수를 변수에 저장하여 가독성을 높임
'''
