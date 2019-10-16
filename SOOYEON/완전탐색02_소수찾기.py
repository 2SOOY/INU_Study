from itertools import permutations
import math

def is_prime(number):
    """
    입력한 숫자가 소수인지 아닌지 판별하는 함수
    input  : number
    return : boolean
    """
    if number == 0 or number == 1:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    # 1. 문자열 한 글자씩 분리된 숫자 문자를 담은 리스트 생성
    numbers = [num for num in numbers]
    possible_set = set()  # 가능한 숫자 조합 집합

    # 2. 숫자 조합 구하기 => 순열 (숫자는 순서가 중요!)
    for pick_num in range(1, len(numbers) + 1):
        # 1개 뽑기 ~ 문자열 길이만큼 뽑기
        permu_set = set(permutations(numbers, pick_num))
        permu_set = set(map(lambda x: ''.join(x), permu_set))  # 분리된 숫자 이어주기
        possible_set |= permu_set  # 숫자 조합에 추가

    # 3. 숫자 집합에 대해 소수 판별
    possible_set = set(map(int, possible_set))  # 문자열 숫자 -> 숫자 변환
    prime_list = list(map(lambda x: is_prime(x), possible_set))  # 소수 판단

    return prime_list.count(True)

