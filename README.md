# PythonPractice

## 까먹을 때마다 확인하는 문법, 주요 함수들
### 1. 빈 리스트 선언
```python
# 방법 1
a = list()

# 방법 2
a = []
```

### 2. 리스트 초기화
```python
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
```

### 3. 리스트 컴프리헨션
리스트 초기화 방법 중 하나로, 대괄호 안에 조건문 & 반복문을 통해 초기화 가능
```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
a = [i for i in range(20) if i % 2 == 1]

# N by M 크기의 2차원 리스트 초기화
# N이 세로, M이 가로
n = 3
m = 5
a = [[0] * m for _ in range(n)]
```

### 4. 리스트 관련 기본 메서드
```python
a = [4, 1, 7]

# append, 시간복잡도 O(1)
# 맨 마지막에 0을 삽입
a.append(0)

# sort(내림차순), 시간복잡도 O(NlogN)
a.sort(reverse = True)

# reverse, 시간복잡도 O(N)
a.reverse()

# insert, 시간복잡도 O(N)
# 1번째 인덱스에 5를 삽입
a.insert(1, 5)

# count, 시간복잡도 O(N)
cnt = a.count(1)

# remove, 시간복잡도 O(N)
# 값이 1인 데이터 하나만 제거
a.remove(1)
```
