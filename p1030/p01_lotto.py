# 로또 맞추기 프로그램을 구현하시오.
# 1. 변수선언
import random

# 2. 6개 번호생성

lotto = random.sample(range(1,46),6)
print(lotto)

# 3. 6개 번호입력

my_num = []
i = 0
while i < 6:
    num = input("{}번째 로또번호를 입력하세요.".format(i+1))
    if not num.isdigit(): # 문자열이 숫자인지 확인해주는 함수
        print("숫자가 아닙니다. 숫자만 입력가능합니다.")
        continue
    num = int(num)
    if 1 <= num <= 45:
        my_num.append(num)
        i += 1
    else:
        print("1~45번까지의 번호를 입력하셔야 합니다.")

print("당첨번호:",lotto)
print("입력번호:",my_num)

# 4. 번호확인

count = 0
c_num = []

for i in my_num:     # [ 5, 9, 11, 12, 36, 40 ]
    if i in lotto:       # 5 -> [ 1, 3, 9, 10, 15, 45 ] # 파이썬만 가능
        c_num.append(i)
        count += 1
            
# for i in lotto:
#     for j in my_num:
#         if i == j:
#             c_num.append(i)
#             count += 1

# 5. 결과출력

print("맞힌번호:",c_num)
print("맞힌개수:",count,"개")

# 6. 당첨금
if count ==0 or count ==1:
    print("당첨금: 0 원")
elif count == 2:
    print("당첨금: 5,000 원")
elif count == 3:
    print("당첨금: 50,000 원")
elif count == 4:
    print("당첨금: 1,000,000 원")
elif count == 5:
    print("당첨금: 50,000,000 원")
elif count == 6:
    print("당첨금: 2,000,000,000 원")
