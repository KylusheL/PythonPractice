# 1. 나의 초견
# 입력
n = int(input())

in_an_hour = ((10 + 6) - 1) * 60 * 2 - ((10 + 6) - 1) ** 2
special_case = 60 * 60

special = (n + 7) // 10
result = (n + 1 - special) * in_an_hour + special_case * special

print(result)

# 2. 책의 풀이
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 3. 얻어갈 점
'''
문제의 의도와 전혀 다르게 풀었다. (수학으로 풀었다.)
if ~ in ~ 의 사용법에 익숙해질 것
str 변환에 익숙해질 것
'''
