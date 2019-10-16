import heapq


def delete_element(heap):
    """
    힙의 종류에 따라 최소힙 -> 최대값 // 최대힙 -> 최소값 제거하는 함수
    INPUT : 최소힙 OR 최대힙
    OUTPUT : 최소값 OR 최대값이 제거된 힙
    """
    heap = list(map(lambda x: -x, heap))
    heapq.heapify(heap)
    heapq.heappop(heap)
    heap = list(map(lambda x: -x, heap))
    heapq.heapify(heap)

    return heap


def solution(operations):
    answer = []
    COMMAND, NUMBER = 0, 1

    max_heap = []
    min_heap = []

    for op in operations:
        op = op.split(' ')
        # 숫자 삽입
        if op[COMMAND] == 'I':
            heapq.heappush(max_heap, -int(op[NUMBER]))
            heapq.heappush(min_heap, int(op[NUMBER]))

        else:
            # 최대값 삭제
            if op[NUMBER] == '1':
                if max_heap:
                    heapq.heappop(max_heap)
                    min_heap = delete_element(min_heap)

            # 최소값 삭제
            else:
                if min_heap:
                    heapq.heappop(min_heap)
                    max_heap = delete_element(max_heap)

    if max_heap and min_heap:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        if max_val == min_val:
            return [0, 0]
        return [max_val, min_val]

    return [0, 0]

