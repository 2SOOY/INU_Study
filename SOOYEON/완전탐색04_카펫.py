def get_width_height(area):
    """
    사각형 면적이 주어질 때, 가능한 가로 세로 길이의 조합을 반환하는 함수
    INPUT :직사각형 면적 (NUMBER)
    OUTPUT : [(가로, 세로), ...] (LIST)
    """
    possible_list = []

    # 면적이 1인 경우
    if area == 1:
        return [(1, 1)]

    # 그 외 경우
    for height in range(1, int(area // 2) + 1):
        if area % height == 0:
            width = area // height
            possible_list.append((width, height))

    return possible_list


def solution(brown, red):
    answer = []
    # 1. 빨간색 타일의 가능한 가로, 세로 조합 구하기
    width_height_set = get_width_height(red)

    # 2-1 1번으로 부터 가능한 총 면적크기를 구하기
    # 2-2 갈색 타일과 빨간색 타일의 면적합을 비교하여 올바른 정답 찾기
    for width, height in width_height_set:
        total_area = ((width + 2) * (height + 2))
        if total_area == brown + red:
            return [width + 2, height + 2]