# 1. 나의 초견
def opposite(s):
    result = ''
    for c in s:
        if c == '(':
            result += ')'
        else:
            result += '('
    return result

def check(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True

def solution(p):
    if p == '':
        return ''
    stack = [p[0]]
    u = ''
    v = ''
    result = ''
    for i in range(1, len(p)):
        if p[i] == stack[-1]:
            stack.append(p[i])
        else:
            stack.pop()
            if len(stack) == 0:
                u = p[:i + 1]
                v = p[i + 1:]
                break
    if check(u):
        result = u + solution(v)
    else:
        result = '(' + solution(v) + ')' + opposite(u[1:-1])
    return result

# 2. 책의 풀이
# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

# 3. 얻어갈 점
'''
생략
'''
