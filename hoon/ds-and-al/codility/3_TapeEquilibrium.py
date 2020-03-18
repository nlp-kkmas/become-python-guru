def solution(A):
	tot = sum(A)
	diff = []

	# P = 1, difference = (13 - 3) - 3
	# P = 2, difference = (13 - (3 + 1)) - (3 + 1)
	# P = 2, difference = (13 - (3 + 1 + 2)) - (3 + 1 + 2)
	tmp = 0
	for elem in A[:-1]:
		tmp += elem
		diff.append(abs(tot - (tmp + tmp)))

	return min(diff)

if __name__ == '__main__':
	print(solution([3, 1, 2, 4, 3]))