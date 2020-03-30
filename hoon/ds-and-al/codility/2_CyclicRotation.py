def solution(A, K):
	n = len(A)

	# Base condition
	if (K == 0) or (n == 0):
		return A

	# K가 n 보다 클 경우, 뺑글뺑글 돌기 때문에 K를 n 보다 작은 수로 만들어줌
	if (K > n):
		q = K // n
		K -= (q * n)

	# Rotation 이후 인덱스에 현재 원소 삽입 인덱스 초과할 경우, 크기만큼 빼주면 됨
	result = [None] * n
	for i, elem in enumerate(A):
		rotated = i + K
		if rotated > n - 1:
			rotated -= n
		result[rotated] = elem

	return result

def solution(A, K):
    n = len(A)
    if n == 0:
        return A
    k = K % n
    return A[n-k:] + A[:n-k]
    
if __name__ == '__main__':
	print(solution([3, 8, 9, 7, 6], 48))