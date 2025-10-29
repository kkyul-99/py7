# 로또번호 맞추기 프로그램
# 1. 변수선언, 로또번호 확인
import random

lotto = (random.sample(range(1,46),6))
print(lotto)

# 2. 숫자입력
my_list = []

for i in range(6):
    num = int(input("숫자를 입력하세요."))
    my_list.append(num)
print("입력번호:",my_list)

# 3. 당첨번호 확인
print("당첨번호:",lotto)
c_list = []

count = 0
for i in lotto:
    for j in my_list:
        if i == j:
            c_list.append(i) # i(로또번호)와 j(입력번호)를 비교하여 같은 것을 c_list에 넣음.
            count += 1

# 4. 결과화면 출력
print("맞춘번호:",c_list)
print("맞춘개수:",count,"개")

# 5. 당첨금 출력
if count == 0 or count ==1:
    print("당첨금: 0원")
elif count == 2:
    print("당첨금: 5,000원")
elif count == 3:
    print("당첨금: 50,000원")
elif count == 4:
    print("당첨금: 1,000,000원")
elif count == 5:
    print("당첨금: 50,000,000원")
elif count == 6:
    print("당첨금: 2,000,000,000원")
