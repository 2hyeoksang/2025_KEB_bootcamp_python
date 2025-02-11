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


