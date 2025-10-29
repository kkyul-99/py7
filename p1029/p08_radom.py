import random

# 1~n 사이에 있는 랜덤숫자 생성
r_num = random.randrange(1,101)
n_list = [] # 저장할 공간
for i in range(5):
    my_num = int(input("숫자를 입력하세요."))
    n_list.append(my_num) # 리스트 추가
    if r_num == my_num:
        print("당첨되었습니다.")
        break
    elif r_num > my_num:
        print("더 큰 수를 입력하세요.")
    else:
        print("더 작은 수를 입력하세요.")
print("당첨번호:",r_num)
print("입력번호:",n_list)

# # randrange() 1~10까지의 랜덤숫자 n개를 출력하시오.
# for i in range(3):
#     print(random.randrange(1,11))
# print(random.sample(range(1,11),5))
