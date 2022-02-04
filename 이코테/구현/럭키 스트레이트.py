# 1. 나의 초견
# 입력
s = input()
half = len(s) // 2
a = s[:half]
b = s[half:]

check = 0
for i in range(half):
    check += int(a[i]) - int(b[i])

result = "LUCKY" if check == 0 else "READY"
print(result)

# 2. 책의 풀이
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")

# 3. 얻어갈 점
'''
문자열 슬라이싱에서 맨 처음부터 자르는 경우, 맨 끝까지 자르는 경우 생략 가능
'''
