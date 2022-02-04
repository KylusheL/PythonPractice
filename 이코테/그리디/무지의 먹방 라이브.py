# 1. 나의 초견
# 1회차) 효율성 테스트 실패
def solution(food_times, k):
    answer = 0
    n = len(food_times)
    pos = 0
    cnt = 0
    while True:
        if food_times[pos] > 0:
            food_times[pos] -= 1
            k -= 1
            cnt += 1
            if k < 0:
                break
        pos += 1
        if pos == n:
            if cnt == 0:
                break
            cnt = 0
            pos = 0
    answer = pos + 1 if cnt != 0 else -1
    return answer

# 2. 책의 풀이

# 3. 얻어갈 점
'''
'''
