def solution(A):
	# N + 1 + 1 개의 None 리스트 생성
	tmp_lst = [None] * (len(A) + 2)

	# A에 존재하는 수는 1로 치환
	for elem in A:
		tmp_lst[elem] = 1

	# 0 인덱스 제거 후, 비어있는 위치의 인덱스 + 1 반환
	return tmp_lst[1:].index(None)

if __name__ == '__main__':
	print(solution([2, 3, 1, 5]))
