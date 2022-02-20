# 1. 나의 초견
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse = True)

result = 0
acc = 0
for i in range(1, n):
    diff = array[i - 1] - array[i]
    if acc + diff * i >= m:
        result = array[i - 1] - int((m - acc) / i)
        break
    else:
        acc += diff * i

print(result)

# 2. 책의 풀이
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)

# 3. 얻어갈 점
'''
접근이 많이 어려웠고, 결국 이진 탐색이 아닌 다른 방법으로 풀었는데, 시간복잡도에 큰 차이는 없는 것 같다. (O(N log N))
테스트케이스가 없어서 확인이 불가능한 점이 아쉽다.
백준 2805번 문제와 동일한 문제라고 한다.
'''
