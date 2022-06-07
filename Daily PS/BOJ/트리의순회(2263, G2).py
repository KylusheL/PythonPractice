import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)     

def pre_order(start, ldx, rdx):
    if ldx > rdx:
        return
    end = start + (rdx - ldx)
    print(post_order[end], end = ' ')
    idx = in_order[post_order[end]]
    pre_order(start, ldx, idx - 1)
    pre_order(start + idx - ldx, idx + 1, rdx)

n = int(input())
in_order = [0] * (n + 1)
for i, num in enumerate(list(map(int, input().split()))):
    in_order[num] = i
post_order = list(map(int, input().split()))
pre_order(0, 0, n - 1)

'''
클래스를 굳이 구현할 필요 없는 문제였다.
인덱스 계산을 신중하게 할 것
재귀 제한 확장 잊지 말 것
'''
