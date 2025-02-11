# base_number = int(input('Input base number : '))
# exponent_number = int(input('Input exponent number : '))
# print(type(base_number), type(exponent_number))
# # f-string
# #print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')
#
# # format function
# print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
# print('밑은 {}, 지수는 {}, 결과 값은 {}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
#
# # c like
# print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))
#
#
# # money = 5,000,000
# # print(money)
# # print(type(money))  # tuple
# # cash = 5_000_000
# # print(cash)
# # print(type(cash))  # int
#
# dec = 65
# octal = 0o101
# hexadecimal = 0x41
# binary = 0b01000001
# print(dec, octal, hexadecimal, binary)
# print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
# print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
# print(ord('B'), ord('Z'), ord('a'), ord('2'))  # 66, 90, 97, 50
# print(hex(dec), hex(octal), hex(hexadecimal), hex(binary))

# 1) for -> while
# 2) while 구문으로 구간 소수 출력하는 프로그램
# 3) ** 대신 pow 함수 사용

import math

def is_prime(num):
    if num >= 2:
        i = 2
        while i <= math.pow(num,0.5) :
            if num % i == 0:
                return False
            i += 1
    else :
        return False
    return True

num = int(input("Enter Integer : "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

num_arr = input("Enter Two Integers : ").split()
num1 = int(num_arr[0])
num2 = int(num_arr[1])

if num1 < num2:
    while num1 <= num2:
        if is_prime(num1):
            print(num1, end = ' ')
        num1 += 1
elif num2 < num1 :
    while num2 <= num1 :
        if is_prime(num2):
            print(num2, end = ' ')
        num2 += 1

# 4) **, pow 함수 쓰지 않고 커스텀 함수를 만들어서..?
def my_power(num, exp):
    result = 1
    for k in range(exp):
        result *= num
    return result