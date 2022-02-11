# 1. 나의 초견
from itertools import combinations

def make_group(arr, idxs):
    result = []
    acc = 0
    for i in range(len(arr)):
        elem = arr[i]
        if i not in idxs:
            acc += elem
        else:
            result.append(acc)
            acc = 0
    if len(result) == 0:
        result.append(acc)
    else:
        result[0] += acc
    result.sort(reverse = True)
    return result
        

def solution(n, weak, dist):
    answer = -1
    dist.sort(reverse = True)
    diff = []
    dangers = len(weak)
    friends = len(dist)
    for i in range(dangers - 1):
        diff.append(weak[i + 1] - weak[i])
    diff.append(n - sum(diff))
    
    for member in range(1, friends + 1):
        validity = False
        for comb in combinations(range(0, dangers), member):
            candidate = make_group(diff, list(comb))
            validity = True
            for i in range(member):
                if candidate[i] > dist[i]:
                    validity = False
                    break
            if validity:
                break
        if validity:
            answer = member
            break
                
    
    return answer

# 2. 책의 풀이
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer

# 3. 얻어갈 점
'''
보류
'''
