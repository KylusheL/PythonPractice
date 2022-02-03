# 1. 나의 초견
# 입력
n = int(input())
coins = list(map(int, input().split()))

coins.sort()
acc = 0 # 현재 만들 수 있는 최대 금액(누적 금액)

for coin in coins:
    if coin > acc + 1: # 누적 금액 + 1보다 큰 동전이 올 때
        break
    else:
        acc += coin

print(acc + 1)

# 2. 책의 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

# 3. 얻어갈 점
'''
n 입력받을 때 int 변환 주의
아이디어는 동일하나, 현재까지의 누적 = 0으로 초기화하는 것보다
타겟 = 1로 초기화하는 편이 깔끔함
break문이 있는 if문은 else가 필요 없음.
'''
