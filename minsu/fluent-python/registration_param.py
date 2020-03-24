# -*- coding: cp949 -*-
# 예제 7-23 매개변수를 받기 위해 함수로 호출되어야 하는 새로운 register() 데커레이터 : registration_param.py

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
