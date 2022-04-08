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

### 5. for문에서 index 점프
```python
# start <= i < end 범위에서 jump만큼 인덱스를 이동하고 싶을 때
for i in range(start, end, jump):
    # do something
```

### 6. 리스트 거꾸로 출력하기
```python
print(my_list[::-1])
```

### 7. 2차원 리스트 복사하기
deepcopy를 사용하지 않으면 b를 수정할 때 a도 같이 수정된다.
```python
import copy
a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)
```

### 8. 빠르게 입력받기
```python
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)
```

### 9. 사용자 정의 비교 함수를 통한 리스트 정렬
```python
from functools import cmp_to_key
my_list = sorted(my_list, key=cmp_to_key(my_cmp))
```

<hr>

## 헷갈릴 수 있는 개념 바로잡기
### 1. 함수, 메서드, 모듈, 패키지, 라이브러리
* 함수: 코드의 집합(자주 사용하게 될 코드)
* 메서드: 클래스 함수라고도 불리며, 클래스 안에 선언된 멤버 함수를 일컫는다. 함수에 포함되는 개념이며, `my_list.sort()`와 같이 온점을 구분자로 하여 실행 가능하다.
* 모듈: 함수 + 클래스 + 변수의 집합이며, .py 확잗자를 갖는다. `import my_module`과 같이 import 명령어를 통해 외부에서 접근 가능
* 패키지: 모듈을 모아둔 폴더이다. `import my_package.my_module`과 같이 외부에서 접근 가능
* 라이브러리: 패키지 및 모듈을 모은 것이다. 패키지와 혼용하여 사용되기도 함.
