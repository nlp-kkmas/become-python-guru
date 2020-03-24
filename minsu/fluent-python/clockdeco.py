# 예제 7-15 함수의 실행 시간을 출력하는 간단한 데커레이터
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:.8f}s] {name}({arg_str}) -> {result}')
        return result
    return clocked
