# 1. 나의 초견
# 입력
s = input()

alph = ''
num = 0

for c in s:
    if c.isdecimal():
        num += int(c)
    else:
        alph += c

alph = ''.join(sorted(alph))
result = alph + str(num)
print(result)

# 2. 책의 풀이
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

# 3. 얻어갈 점
'''
isdigit(), isdecimal(), isnumeric(), isalpha() 메서드
리스트의 문자열화 my_str = ''.join(my_list)
sort() 메서드는 문자열에 적용 불가능
'''
