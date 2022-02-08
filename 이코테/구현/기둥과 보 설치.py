# 1. 나의 초견
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        check = False        
        x, y, a, b = frame
        print(x, y, a, b)
        L = [x - 1, y, 1] in answer
        R = [x, y, 1] in answer
        D = [x, y - 1, 0] in answer
        U = [x, y, 0] in answer
        LL = [x - 2, y, 1] in answer
        LD = [x - 1, y - 1, 0] in answer
        LU = [x - 1, y, 0] in answer
        RR = [x + 1, y, 1] in answer
        RD = [x + 1, y - 1, 0] in answer
        RU = [x + 1, y, 0] in answer
        UL = [x - 1, y + 1, 1] in answer
        UR = [x, y + 1, 1] in answer
        UU = [x, y + 1, 0] in answer
        ULL = [x - 2, y + 1, 1] in answer
        URR = [x + 1, y + 1, 1] in answer
        RRD = [x + 2, y - 1, 0] in answer
        if b == 1: # 설치
            if a == 0: # 기둥을
                check = (y == 0) or L or R or D
            else: # 보를
                check = D or RD or (L and RR)
            # 확인 후 설치
            if check:
                answer.append(frame[0:3])
        else: # 제거
            if a == 0: # 기둥을
                if UU:
                    if not (UL or UR):
                        continue
                if UL:
                    if not (LU or (ULL and UR)):
                        continue
                if UR:
                    if not (RU or (UL and URR)):
                        continue
            else: # 보를
                if U:
                    if not (L or D):
                        continue
                if RU:
                    if not (RD or RR):
                        continue
                if L:
                    if not (LD or D):
                        continue
                if RR:
                    if not (RD or RRD):
                        continue
            answer.remove(frame[0:3])
    answer.sort()
    return answer

# 2. 책의 풀이
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환

# 3. 배워갈 점
'''
완전탐색 노가다로 풀었다. 하지만 필요한 부분만 확인했다.
하지만 제한 시간이 충분하므로, 설치 또는 제거를 먼저 해본 뒤 유효성을 확인하는 방법이 직관적일 수 있다.
'''
