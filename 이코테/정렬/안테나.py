# 1. 나의 초견
n = int(input())
data = list(map(int, input().split()))
count = [0] * (max(data) + 1)
for house in data:
    count[house] += 1

target = int((n + 1) / 2)
for i in range(len(count)):
    target -= count[i]
    if target <= 0:
        print(i)
        break
        
# 2. 책의 풀이
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])

# 3. 얻어갈 점
'''
굳이 계수정렬로 구현 안해도 된다.
'''
