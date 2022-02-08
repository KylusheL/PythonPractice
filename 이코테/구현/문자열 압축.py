# 1. 나의 초견
def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n // 2 + 1):
        j = 0
        count = 1
        candidate = s[0 : i]
        new_s = ''
        while True:
            j += i
            if j + i > n:
                new_s += str(count) if count > 1 else ''
                new_s += candidate
                new_s += s[j : ]
                break
            if candidate == s[j : j + i]:
                count += 1
            else:
                new_s += str(count) if count > 1 else ''
                new_s += candidate
                candidate = s[j : j + i]
                count = 1
        if len(new_s) < answer:
            answer = len(new_s)

    return answer

# 2. 책의 풀이
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

# 3. 얻어갈 점
'''
자르는 단위를 step이라는 직관적인 변수로 이름지은 것
for문 range의 세번째 인자 적절히 사용한 것
min 함수의 활용
'''

# 4. 번외 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

'''
잘라진 단어들을 리스트에 담은 뒤, 인덱스 1 차이에서 zip을 이용하여 비교
'''
