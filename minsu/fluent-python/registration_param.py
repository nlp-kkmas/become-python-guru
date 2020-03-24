# -*- coding: cp949 -*-
# ���� 7-23 �Ű������� �ޱ� ���� �Լ��� ȣ��Ǿ�� �ϴ� ���ο� register() ��Ŀ������ : registration_param.py

registry = set()

def register(active=True):
    def decorate(func):
        print(f'running register(active={active})->decorate{func}')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
            
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')
