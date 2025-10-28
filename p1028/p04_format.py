# 이름, 국어, 영어, 수학 점수를 입력받아
# 홍길동, 국어, 영어, 수학, 합계, 평균을 출력하시오.

# name = input("이름을 입력하세요.")
# kor = int(input("국어 점수를 입력하세요."))
# eng = int(input("영어 점수를 입력하세요."))
# math = int(input("수학 점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# score = [name, kor, eng, math, total, avg]
# print("이름: {}, 국어: {}, 영어: {}, 수학: {}, 합계: {}, 평균: {:.2f}".format(*score))

a_list = ['홍길동', 100, 90, 80, 270, 90.00000]
print("이름: {}, 국어: {}, 영어: {}, 수학: {}, 합계: {}, 평균: {:.2f}".format\
    (a_list[0],a_list[1],a_list[2],a_list[3],a_list[4],a_list[5]))
print("이름: {}, 국어: {}, 영어: {}, 수학: {}, 합계: {}, 평균: {:.2f}".format\
    (*a_list)) # 전개연산자 - list 안의 데이터를 순서대로 표시

a = 10
b = 20
print("1번째값: {:1}, 2번째값: {:0}".format(a,b))    # *******
print(f"1번째값: {b}, 2번째값: {a}")

# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# n1 = int(input("금액을 입력하세요."))
# n2 = int(input("금액을 입력하세요."))
# n3 = int(input("금액을 입력하세요."))
# total = n1+n2+n3
# print("1번금액: {:,d} 원\n2번금액: {:,d} 원\n3번금액: {:,d} 원\n총금액: {:,d} 원".format(n1,n2,n3,total))

# year = 2025
# month = 10
# day = 28
# print("%d 년 %03d 월 %d 일" % (year, month, day))
# day_format = "{:,d} 년 {:03d} 월 {} 일".format(year, month, day) # 1,000단위 표시 가능(%는 불가능)
# print(day_format)
