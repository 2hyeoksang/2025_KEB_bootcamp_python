import time
# v3.6) 2중 데코레이터 적용. 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오.

#SOLID
#Open Closed Principal : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)

def description_decorator(f):
    def inner(*arg):
        print(f.__name__)
        print(f.__doc__)
        # r = f(*arg)
        # return r
    return inner


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e-s}')
        return r
    return wrapper


# @description_decorator
# @time_decorator
def factorial(n):
    """
    calculating the value of factorial of n
    """
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result


number=int(input("num : "))
t = description_decorator(factorial)
t(number)
print(f'{number}! = {time_decorator(factorial)(number)}')
