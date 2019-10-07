def solution(clothes):
    # 1. 주어진 정보를 바탕으로 자료 구성
    clothes_info = {} # 의상 타입(key): 의상 수(value)
    for c_name, c_type in clothes:
        clothes_info[c_type] = clothes_info.get(c_type, 0) + 1
    
    # 2. 경우의 수 구하기
    result = 1 # 조합 가능한 경우의 수
    # a1, a2, a3, b1, b2 의상이 존재할 때 경우의 수
    # (3 + 1) * (2 + 1) - 1 
    # +1의 이유는 착용을 안하는 경우
    # 마지막 -1의 경우는 문제에서 제시된 최소 하나는 착용한다
    for value in clothes_info.values():
        result *= value + 1
    
    return result - 1
