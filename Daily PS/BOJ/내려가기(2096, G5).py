import copy
import sys
input = sys.stdin.readline

n = int(input())
max_arr = [0, 0, 0]
min_arr = [0, 0, 0]
for _ in range(n):
    data = list(map(int, input().split()))
    max_tmp = copy.deepcopy(data)
    max_tmp[0] += max(max_arr[:2])
    max_tmp[1] += max(max_arr)
    max_tmp[2] += max(max_arr[1:])
    min_tmp = copy.deepcopy(data)
    min_tmp[0] += min(min_arr[:2])
    min_tmp[1] += min(min_arr)
    min_tmp[2] += min(min_arr[1:])
    max_arr = max_tmp
    min_arr = min_tmp

print(max(max_arr), min(min_arr))

'''
dp 기초문제
dp 테이블을 전부 만들지 않고 풀 수 있다.
'''
