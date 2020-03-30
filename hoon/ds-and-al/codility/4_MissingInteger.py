def solution(A):
	A = [elem for elem in A if elem > 0]

	# Only-negatives case:
	if len(A) == 0:
		return 1

	record = {i+1: False for i in range(max(A))}
	for elem in A:
		record[elem] = True

	key = None
	for key, elem in record.items():
		if not elem:
			return key

	return key + 1


if __name__ == '__main__':
	# print(solution([1, 3, 6, 4, 1, 2]))  # 5
	# print(solution([1, 2, 3]))  # 4
	# print(solution([-1, -3]))  # 1
	print(solution([-89] + list(range(101))))  # 1