# 990101-1111111
# 870001-2111111
# 071001-4111111

# 1 - 남자, 2 - 여자
# 주민번호를 입력받아, 남자인지 여자인지 출력하시오.
jumin = input("주민번호를 입력하세요.")
num1 = int(jumin[7])
if num1 == 1 or num1 == 3:
    print("남자입니다.")
if num1 == 2 or num1 == 4:
    print("여자입니다.")

import datetime
now = datetime.datetime.now()
month = now.month

num2 = int(jumin[2:4])
if num2 == month:
    print("이벤트에 당첨되셨습니다.")
else:
    print("이벤트에 당첨되지 않았습니다.")
