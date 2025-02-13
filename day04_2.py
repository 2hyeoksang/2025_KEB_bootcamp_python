import random

drinks=['위스키', '와인', '소주', '고량주','데킬라']
foods = ['초콜릿', '치즈', '삼겹살', '양꼬치','라임']
price = [50000,30000,5000,7500,35000]

japan_drinks = ['사케', '위스키']
japan_foods = ['광어회', '낙곱새']
price.append(25000)

for drink, food in zip(japan_drinks, japan_foods) :
    if drink in drinks :
        foods[drinks.index(drink)] = food
    else:
        drinks.append(drink)
        foods.append(food)

amounts = [0 for i in range(len(drinks))]

# print(drinks)
# print(foods)

menu_list = '다음 술 중에 고르시오.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}) {drinks[i]}     '
menu_list = menu_list + f'{len(drinks)+1}) 아무거나     {len(drinks)+2}) 종료 : '

total_price = 0

def print_menu(menu):
    global total_price
    try :
        print(f'{drinks[menu - 1]}에 어울리는 안주는 {foods[menu - 1]} 입니다.')
        print(f'{price[menu - 1]} 원입니다.')
        total_price += price[menu - 1]
        amounts[menu - 1] += 1
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
        elif 1 <= menu :
            print_menu(menu)
        else:
            print('잘못된 입력입니다.')
        print()
    except :
        print('잘못된 입력입니다.')


#print(amounts)
print()
for k in range(len(drinks)):
    if amounts[k] != 0:
        print(f'주류명 : {drinks[k]}, 수량 : {amounts[k]}, 단가 : {price[k]}, 소계 : {price[k]*amounts[k]}')

print(f'\n총 금액 : {total_price}')
