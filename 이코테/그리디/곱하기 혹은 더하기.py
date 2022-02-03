# 1. 나의 초견
# 입력
s = input()

result = 0

for num in s:
    num = int(num)
    if num > 1 and result > 1:
        result *= num
    else:
        result += num

print(result)

# 2. 책의 풀이
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 3. 얻어갈 점

'''
result = 1 일 경우에도 곱하기보다 더하기를 선택해야하는 부분 간과했음.
result를 스트링의 맨 앞자로 초기화하는 방법도 있음.
'''
