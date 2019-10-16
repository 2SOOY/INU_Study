# 순서가 중요함
# 1번 5번마다 반복
# 2번 8번마다 반복
# 3번 10번마다 반복

def solution(answers):
    
    # 1. 주어진 정보를 바탕으로 자료 구성
    correct_count = {} # 사람(key): 문제 맞춘 수(value)를 담을 딕셔너리
    
    person_1 = "12345"
    person_2 = "21232425"
    person_3 = "3311224455"
    
    P1_LEN = len(person_1)
    P2_LEN = len(person_2)
    P3_LEN = len(person_3)
    
    P1, P2, P3 = 1, 2, 3
    COUNT, PERSON = 0, 1
    
    answers = ''.join(map(str, answers)) # 정답번호 배열을 문자열 처리
    
    # 2. 문제를 맞춘 사람 count 증가
    for idx, answer in enumerate(answers):
        
        if answer == person_1[idx % P1_LEN]:
            correct_count[P1] = correct_count.get(P1, 0) + 1
        
        if answer == person_2[idx % P2_LEN]:
            correct_count[P2] = correct_count.get(P2, 0) + 1
        
        if answer == person_3[idx % P3_LEN]:
            correct_count[P3] = correct_count.get(P3, 0) + 1
    
    # 3. 딕셔너리 정보를 바탕으로 문제를 가장 많이 맞춘사람을 구해 리턴
    result = sorted([(-count, person) for person, count in correct_count.items()]) # count는 내림차순 & person은 오름차순
    max_count = max(correct_count.values())
    
    return [person for count, person in result if -count == max_count]# 순서가 중요함
# 1번 5번마다 반복
# 2번 8번마다 반복
# 3번 10번마다 반복

def solution(answers):
    
    # 1. 주어진 정보를 바탕으로 자료 구성
    correct_count = {} # 사람(key): 문제 맞춘 수(value)를 담을 딕셔너리
    
    person_1 = "12345"
    person_2 = "21232425"
    person_3 = "3311224455"
    
    P1_LEN = len(person_1)
    P2_LEN = len(person_2)
    P3_LEN = len(person_3)
    
    P1, P2, P3 = 1, 2, 3
    COUNT, PERSON = 0, 1
    
    answers = ''.join(map(str, answers)) # 정답번호 배열을 문자열 처리
    
    # 2. 문제를 맞춘 사람 count 증가
    for idx, answer in enumerate(answers):
        
        if answer == person_1[idx % P1_LEN]:
            correct_count[P1] = correct_count.get(P1, 0) + 1
        
        if answer == person_2[idx % P2_LEN]:
            correct_count[P2] = correct_count.get(P2, 0) + 1
        
        if answer == person_3[idx % P3_LEN]:
            correct_count[P3] = correct_count.get(P3, 0) + 1
    
    # 3. 딕셔너리 정보를 바탕으로 문제를 가장 많이 맞춘사람을 구해 리턴
    result = sorted([(-count, person) for person, count in correct_count.items()]) # count는 내림차순 & person은 오름차순
    max_count = max(correct_count.values())
    
    return [person for count, person in result if -count == max_count]
