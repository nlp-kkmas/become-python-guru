# 예제 7-17 개선된 clock 데커레이터
# clockdeco2.py

import time
import functools

def clock(func):
    @functools.wraps(func) # 표준 라이브러리에서 제공하는 데커레이터 중 하나.
    def clocked(*args, **kwargs): # keyword 인수를 지원.
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:.8f}] {name}({arg_str}) -> {result}')
        return result
    return clocked