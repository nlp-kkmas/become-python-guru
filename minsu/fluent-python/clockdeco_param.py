# -*- coding: cp949 -*-
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):                 # �Ű�����ȭ�� ��Ŀ������ ���丮
    def decorate(func):                     # ���� ��Ŀ������
        def clocked(*_args):                # ��Ŀ����Ʈ�� �Լ��� ����
            t0 = time.time()
            _result = func(*_args)          # ��Ŀ����Ʈ�� �Լ��� ����� ����
            elapsed = time.time() - t0 
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
#             print('args :', args)         # args : 0.123
            result = repr(_result)
            print(fmt.format(**locals()))   # fmt�� clocked()�� ���� ������ ��� ������ �� �ְ� ���ش�.
            return _result
        return clocked
    return decorate
