import sys
input = sys.stdin.readline

s = input().rstrip()
target = input().rstrip()
stack = []
for elem in s:
    stack.append(elem)
    if stack[-1] == target[-1] and len(stack) >= len(target):
        if ''.join(map(str, stack[-len(target):])) == target:
            for _ in range(len(target)):
                stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(map(str, stack)))
    
'''
결국 해답 봄
스택의 활용에 익숙하지 못한 것 같다.
때로는 재귀 말고 스택을 써야 하는 상황을 떠올려보자.
'''
