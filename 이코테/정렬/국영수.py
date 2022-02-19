# 1. 나의 초견
from functools import cmp_to_key

n = int(input())
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

def kys(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    else:
        if x[2] < y[2]:
            return -1
        elif x[2] > y[2]:
            return 1
        else:
            if x[3] > y[3]:
                return -1
            elif x[3] < y[3]:
                return 1
            else:
                if x[0] < y[0]:
                    return -1
                else:
                    return 1

array = sorted(array, key=cmp_to_key(kys))
for student in array:
    print(student[0])
    
# 2. 책의 풀이
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
    
# 3. 얻어갈 점
'''
람다함수 사용법에 더 친숙해질 것
정렬 기준으로 람다함수를 쓸 때 우선순위 설정 가능, 자료형 변환 가능, 오름/내림차순 설정 가능
'''
