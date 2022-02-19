# 1. 나의 초견
def solution(N, stages):
    stay = [0] * (N + 2)
    for stage in stages:
        stay[stage] += 1
    players = len(stages)
    fail_rate = []
    for i in range(1, N + 1):
        if players == 0:
            fail_rate.append((i, 0))
        else:
            fail_rate.append((i, stay[i] / players))
        players -= stay[i]
    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    answer = []
    for info in fail_rate:
        answer.append(info[0])
    return answer

# 2. 책의 풀이
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer

# 3. 얻어갈 점
'''
리스트 컴프리헨션 잘 활용할 것
count 함수 이용하기
'''
