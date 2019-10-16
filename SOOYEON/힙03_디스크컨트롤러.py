import heapq


def solution(jobs):
    answer = 0
    REQ, NEED = 0, 1
    CHECK = 1

    # 1. 요청 순서가 빠른 순으로 작업 정렬
    jobs = sorted(jobs, key=lambda x: (x[REQ], x[NEED]))
    jobs_check = [0] * len(jobs)  # 해당 작업에 대해 처리 여부 확인을 위한 리스트
    total_time = 0  # 현재까지 소요된 시간
    work_heap = []  # 일을 진행하고 있을 때 다음 가능한 일을 담을 힙
    complete_time = []  # 각 작업이 완료되는데 소요된 시간
    index = 0

    # 2. 모든 일을 순회 => 체크 여부 판단
    while jobs_check[index] != CHECK:

        # 2-1. 일거리가 있는 경우
        if work_heap:
            # 일 선택하기 => 소요시간이 짧은 일을 우선으로
            while work_heap:
                now_need, now_req = heapq.heappop(work_heap)
                total_time += now_need
                complete_time.append(total_time - now_req)

                # 가능한 일 담기
                for idx, job in enumerate(jobs[index:]):
                    if total_time >= job[REQ]:
                        heapq.heappush(work_heap, (job[NEED], job[REQ]))
                        jobs_check[index] = CHECK
                        index += 1

        # 2-2. 일거리가 없는 경우
        else:
            # 힙에 채워넣기
            heapq.heappush(work_heap, (jobs[index][NEED], jobs[index][REQ]))
            jobs_check[index] = CHECK
            total_time = jobs[index][REQ]
            index += 1

        # 인덱싱 처리
        if index == len(jobs):
            break

    # 3. 힙에 일거리가 남아있는 경우 처리
    if work_heap:
        need, req = heapq.heappop(work_heap)
        total_time += need
        complete_time.append(total_time - req)

    return sum(complete_time) // len(jobs)