# 풀이 1 - Counter 이용
from collections import Counter

def solution(participant, completion):
    # Counter를 이용하면 리스트 내의 성분의 숫자를 딕셔너리 형태로 반환해준다
    # ex) list1 =['a', 'b', 'c', 'a'] => Counter(list1) : {'a':2, 'b':1, 'c':1}
    not_completion = Counter(participant) - Counter(completion) # Counter의 경우 사칙연산도 가능
     
    return list(not_completion.keys())[0]
