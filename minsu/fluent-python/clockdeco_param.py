# -*- coding: cp949 -*-
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):                 # 매개변수화된 데커레이터 팩토리
    def decorate(func):                     # 실제 데커레이터
        def clocked(*_args):                # 데커레이트된 함수를 래핑
            t0 = time.time()
            _result = func(*_args)          # 데커레이트된 함수의 결과를 저장
            elapsed = time.time() - t0 
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
#             print('args :', args)         # args : 0.123
            result = repr(_result)
            print(fmt.format(**locals()))   # fmt가 clocked()의 지역 변수를 모두 참조할 수 있게 해준다.
            return _result
        return clocked
    return decorate
