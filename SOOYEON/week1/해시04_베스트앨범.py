def solution(genres, plays):
    GEN, PLAY = 0, 1 # 장르, 재생횟수
    VALUE = 1        # 딕셔너리에서 value의 인덱스
    
    # 1. 주어진 정보 배열들을 알맞게 조작하기
    song_info = [(gen, play) for gen, play in zip(genres, plays)]
    
    dic_songs = {} # 장르(key): 노래정보(고유번호, 재생횟수)
    dic_plays = {} # 장르(key): 재생횟수 합
    for idx, info in enumerate(song_info):
        dic_songs[info[GEN]] = dic_songs.get(info[GEN], []) + [(idx, info[PLAY])]
        dic_plays[info[GEN]] = dic_plays.get(info[GEN], 0) + info[PLAY]
    
    
    # 2. 장르별 재생횟수 합이 높은 순서대로 정렬
    dic_plays = sorted(dic_plays.items(), key=lambda x: x[VALUE], reverse=True)
    
    
    result = [] # 정답 배열
    
    # 3. 2단계에서 구한 정보를 바탕으로 각 장르에서 재생횟수가 높은 2가지 음악 번호 배열에 담기
    for gen, plays in dic_plays:
        best_songs = dic_songs.get(gen) # best_songs = [(고유번호, 재생횟수), ...]
        best_songs = sorted(best_songs, key=lambda x: x[PLAY], reverse=True)
        if len(best_songs) >= 2 : # 해당 장르의 곡이 2개 이상일 경우
            for idx in range(2):
                result.append(best_songs[idx][0])
        else: # 2개보다 작으면 전부 다 넣어
            for idx in range(len(best_songs)):
                result.append(best_songs[idx][0])
        
    return result
