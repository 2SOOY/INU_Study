import heapq


def solution(scovilles, K):
    mix_num = 0  # 섞은 횟수

    # 1. heap정렬 (python min_heap)
    heapq.heapify(scovilles)

    # 2. 모든 음식의 스코빌 지수가 K이상이 되도록 조작
    while scovilles[0] < K:  # 최소값이 K보다 작으면 반복
        # 예외 조건 : 불가능한 경우 -1 리턴
        if len(scovilles) == 1:
            return -1

        # 2-1. 2가지 음식 뽑기
        first_K = heapq.heappop(scovilles)
        second_K = heapq.heappop(scovilles)

        # 2-2. 음식 섞기
        new_K = first_K + (second_K * 2)
        mix_num += 1

        # 2-3. 해당 음식 다시 scovilles 배열에 삽입
        heapq.heappush(scovilles, new_K)

    return mix_num
