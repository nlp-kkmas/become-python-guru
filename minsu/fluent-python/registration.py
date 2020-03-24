# 예제 7-2 registration.py 모듈
registry = []    # registry 배열은 @register로 데커레이트된 함수들에 대한 참조를 담는다.

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
    
@register
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')
    
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
    
if __name__=='__main__':
    main()