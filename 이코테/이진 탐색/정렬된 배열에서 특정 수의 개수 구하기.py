# 1. 나의 초견
n, x = map(int, input().split())
array = list(map(int, input().split()))

def bi_search_left(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            if array[mid] == target:
                result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

def bi_search_right(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            if array[mid] == target:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

left = bi_search_left(array, x, 0, n - 1)
right = bi_search_right(array, x, 0, n - 1)
if left == -1:
    print(-1)
else:
    print(right - left + 1)
    
# 2. 책의 풀이
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
    
# 3. 얻어갈 점
'''
bisect_left, bisect_right 라이브러리 활용에 익숙해지면 좋다.
bisect_right의 경우 해당 원소를 삽입할 위치를 알려주므로, 가장 오른쪽 원소보다 한 칸 더 오른쪽의 인덱스를 반환
'''
