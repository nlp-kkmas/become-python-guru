def solution(A):
	record = {i+1: None for i in range(len(A))}

	for elem in A:
		record[elem] = 1

	for elem in record.values():
		if elem is None:
			return 0
	return 1


if __name__ == '__main__':
	print(solution([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]))