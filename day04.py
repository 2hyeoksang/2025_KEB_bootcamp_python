# subjects = ["데이터베이스", "C++", "5", "Java", "Python", "Java", "9", "리눅스"]
# print(subjects[::-1])
# #subjects[::-1]
# #subjects = subjects[::-1]  # subjects.reverse()
# print(subjects)
# #subjects.remove("Java")
# #del subjects[-2]
# #del subjects[2]
# subjects.pop(2)
# #subjects.sort(reverse=True)  # desc
# copy_subjects = sorted(subjects)
# print(subjects)
# print(copy_subjects)

# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)

# # squares = list()
# # for i in range(1, 6, 1):
# #     squares.append(i*i)
# # print(squares)
#
# #list comprehension
# squares = [i*i for i in range(1, 6, 1)]
# print(squares)
#
# even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
# print(even_squares)


# sugang = dict(python="kim", cpp="sung", db="kang")
# # print(sugang)
# # sugang['datastructure'] = 'kim'  # add
# # print(sugang)
# # sugang['datastructure'] = 'park'  # update
# # print(sugang)
# # print(sugang['db'])
# # print(sugang.get('db'))
# # print(sugang.get('opensource'))
# # print(sugang.get('opensource', 'not exist'))
# for subject, professor in sugang.items():
#     print(f'{subject} 과목 담당교수는 {professor}입니다')
#
# #for k in sugang.keys():
# for k in sugang:
#     print(k)
#
# for v in sugang.values():
#     print(v)
#
# for s in sugang.items():
#     print(s)

# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
#
# #drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# #print(drinks_foods_keys)
#
# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'다음에 또 오세요')
#         break

import random

drinks=['위스키', '와인', '소주', '고량주','데킬라']
foods = ['초콜릿', '치즈', '삼겹살', '양꼬치','라임']

japan_drinks = ['사케', '위스키']
japan_foods = ['광어회', '낙곱새']

for drink, food in zip(japan_drinks, japan_foods) :
    if drink in drinks :
        foods[drinks.index(drink)] = food
    else:
        drinks.append(drink)
        foods.append(food)

# print(drinks)
# print(foods)

menu_list = '다음 술 중에 고르시오.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}     '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나     {len(drinks)+2}) 종료 : '


def print_menu(menu):
    try :
        print(f'{drinks[menu - 1]}에 어울리는 안주는 {foods[menu - 1]} 입니다.')
    except IndexError :
        print("없는 메뉴입니다.")


while True:
    try:
        menu = int(input(menu_list))
        if menu == len(drinks)+2:
            print('다음에 또 오세요.')
            break
        elif menu == len(drinks)+1:
            random_idx = random.randint(1, len(drinks))
            print_menu(random_idx)
        else :
            print_menu(menu)
        print()
    except :
        print()
    # if menu == '1':
    #     print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    # elif menu == '2':
    #     print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    # elif menu == '3':
    #     print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
    # elif menu == '4':
    #     print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    # elif menu == '5':
    #     print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
    # elif menu == '6':
    #     random_idx = random.randint(0, len(drinks)-1)
    #     print(f'{drinks[random_idx]}에 어울리는 안주는 {foods[random_idx]} 입니다')
    # elif menu == '7':
    #     print(f'다음에 또 오세요')
    #     break


# import random
# star = ['테란', '저그', '프로토스']
# print(random.choice(star))
# print(random.randint(1,6))
# print(star[random.randint)

# univ = 'inha university'
# cnt_alphabet = {letter : univ.count(letter) for letter in univ}
# # cnt_alphabet = [ [letter, univ.count(letter)] for letter in univ]
# print(cnt_alphabet,len(cnt_alphabet))

