# 1. 나의 초견

# 입력
n = int(input())
a = list(map(int, input().split()))
a.sort()

group = 0
result = 0

# 공포도가 낮은 사람부터 그룹 구성
for fear in a:
    group += 1
    if fear <= group:
        result += 1
        group = 0

print(result)

# 2. 책의 풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력

# 3. 얻어갈 점

'''
성급하지 말고 풀이가 확실한지 꼼꼼히 살피자.
'''
