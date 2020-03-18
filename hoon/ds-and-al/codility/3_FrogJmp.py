import math

def solution(X, Y, D):
	Y -= X
	return math.ceil(Y / D)