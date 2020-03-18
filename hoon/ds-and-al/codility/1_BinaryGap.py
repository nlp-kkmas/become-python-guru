def solution(N):
    # 정수를 이진수로 변환
    binary = bin(N)[2:]
    max_dist = 0

    # 모든 1을 저장하기 위해 딕셔너리 정의
    h = {i:val for i, val in enumerate(binary) if val == '1'}
    
    ones = list(reversed(list(h.keys())))

    # 1의 위치가 저장된 인덱스 리스트를 돌며, 최대 거리 계산 후 반환
    for i in range(len(ones) - 1):
        dist = ones[i] - ones[i+1] - 1
        if dist > max_dist: max_dist = dist
            
    return max_dist