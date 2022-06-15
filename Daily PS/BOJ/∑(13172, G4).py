import sys
input = sys.stdin.readline
X = 1000000007

def power(x, y):
    if y == 1:
        return x
    tmp = 1
    if y % 2 == 1:
        tmp *= x
    half = power(x, y // 2)
    return (tmp * half * half) % X

t = int(input())
result = 0
for _ in range(t):
    a, b = map(int, input().split())
    result += b * power(a, X - 2) % X
    result %= X

print(result)
