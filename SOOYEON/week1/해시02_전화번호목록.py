# 시간복잡도 O(n^2)

def solution(phone_book):
    # phone_book 전체를 반복 => 기준 설정
    for phone_num in phone_book:
        # 반복문을 통해 나머지 번호들과 비교
        for compare_num in phone_book:
            if phone_num == compare_num:
                continue
            # 접두어 확인
            # ex) '119','1195524421' 비교
            # '1195524421'에서 '119'길이(3) 원소까지만 비교
            if phone_num in compare_num[:len(phone_num)]:
                return False
    
    return True 
