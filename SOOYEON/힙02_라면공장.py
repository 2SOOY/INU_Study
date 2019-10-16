import heapq


def solution(stock, dates, supplies, k):
    # 1. 변수 선언 및 데이터 조작
    answer = 0  # 정답
    overseas_info = list(zip(dates, supplies))  # (공급일, 공급량) 정보가 담긴 리스트
    max_heap = []  # 공급받기 가능한 정보를 담은 최대힙

    # 2. 로직 구현
    # stock을 누적하는 방식 => k에 도달하기전까지 반복행위
    # stock과 date를 비교하여 stock값이 크다면 해당 밀가루를 공급받을 수 있음을 뜻함
    # ex) stock = 4   -----  date1 = 1, date2 = 3, date3 = 4, date4 = 8
    #   => date1, date2, date3인 업체로 부터 공급받기 가능

    while stock < k:  # stock이 k보다 크거나 같으면 공급받을 필요 없음
        next_idx = 0  # 반복 범위를 조절할 idx

        if overseas_info:  # 이 조건문 때문에 정확성에서 실패하였음
            for idx, (date, supply) in enumerate(overseas_info):
                if stock >= date:  # 공급 받을 수 있는 목록들
                    heapq.heappush(max_heap, (-supply, date))  # 최대힙에 넣기
                    next_idx = idx + 1  # 다음 조사할 범위 갱신
                else:
                    break
            overseas_info = overseas_info[next_idx:]  # 다음 조사 범위

        stock -= heapq.heappop(max_heap)[0]  # max_heap으로부터 공급량이 많은 것들을 우선으로 공급받음
        answer += 1  # 공급 받았으면 횟수 카운트

    return answer