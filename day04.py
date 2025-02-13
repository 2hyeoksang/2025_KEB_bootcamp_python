# def out_func(nout):
#     def inner_func():
#         return nout * nout
#     return inner_func
#
#
# x = out_func(9)
# print(type(x))
# print(x)
# print(x())
import time


# nums=['7', '-11', '3']
#
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
#
# print(nums)

#SOLID
#Open Closed Principal : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)
def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e-s}')
        return r
    return wrapper

#@time_decorator
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

number = int(input('num : '))
# s = time.time()
ft = time_decorator(factorial)
print(f"{number}! = {ft(number)}")

number=int(input("num : "))
print(f'{number}! = {factorial(number)}')
# e = time.time()
# print(e-s)