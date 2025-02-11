import math

num = int(input("수를 입력하시오."))

# t1 = 0
# for i in range(2,num):
#     if num % i == 0 :
#         t1 = 1
#         break
#
# if t1 == 1 or num == 1 :
#     print("합성수입니다.")
# else:
#     print("소수입니다.")

# t1 = True
# for i in range(2,int(math.sqrt(num)+1)):
#     if num % i == 0 :
#         t1 = False
#         break
#
# if t1 == False or num == 1:
#     print("합성수입니다.")
# else:
#     print("소수입니다.")

def is_prime(num) -> bool :
    '''
    소수 판별
    :param num: integer number
    :return: bool type
    '''
    if num >= 2:
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0 :
                return False

    else :
        return False
    return True

if is_prime(num):
    print("Prime")
else:
    print("NOT Prime")

help(is_prime)