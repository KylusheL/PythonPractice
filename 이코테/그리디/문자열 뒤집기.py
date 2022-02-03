# 1. 나의 초견
# 입력
s = input()

result = 0
now = -1
for c in s:
    c = int(c)
    if c != now:
        now = c
        result += 1
print(result // 2)

# 2. 책의 풀이
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

# 3. 얻어갈 점
'''
규칙성을 찾아 식을 만든 뒤 문법으로 옮기기만 하면 더 쉽게 풀 수 있다.
'''
