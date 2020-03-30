def solution(X, A):
	leaves = {i+1: -1 for i in range(X)}
	
	for idx, num in enumerate(A):
		if num in leaves:
			del leaves[num]
		if len(leaves) == 0:
			return idx
	return -1


if __name__ == '__main__':
	print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))