def solution(A):
    h = {}
    for val in A:
        try:
            h[val] = not h[val]
        except KeyError:
            h[val] = True
    
    for val in h:
        if h[val]: 
            return val