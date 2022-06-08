import sys
input = sys.stdin.readline

rank = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
stack = []
expr = input().rstrip()
expr = '(' + expr + ')'
result = ""
for i in range(len(expr)):
    if expr[i].isalpha():
        result += expr[i]
    else:
        if expr[i] == '(':
            stack.append(expr[i])
        elif expr[i] == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while rank[expr[i]] <= rank[stack[-1]]:
                result += stack.pop()
            stack.append(expr[i])

print(result)

'''
스택을 이용해서 더 어려운 계산기까지 구현했었는데
간만에 다시 하려니 간단한 것도 헷갈렸다.
우선순위 처리랑 괄호처리 깔끔하게 하는 방법에 대해 좀 더 고민해볼 것
'''
