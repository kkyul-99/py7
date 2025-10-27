# 국어, 영어, 수학 점수를 입력받아
# 합계, 평균을 출력하시오.
# 합계: 299
# 평균: 99.97 소수점 2자리 출력

# score1 = int(input("국어 점수를 입력하세요."))
# score2 = int(input("영어 점수를 입력하세요."))
# score3 = int(input("수학 점수를 입력하세요."))
# print("합계: %d" % (score1+score2+score3))
# print("평균: %.2f" % ((score1+score2+score3)/3))

# \t: 탭키-사이띄움, \n: 줄바꿈
# print("안녕\t하\n세요.")
name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
# print("합계: %d" % (kor+eng+math))
# print("평균: %.2f" % ((kor+eng+math)/3))
total = (kor+eng+math)
avg = (kor+eng+math)/3

name2 = input("이름을 입력하세요.")
kor2 = int(input("국어 점수를 입력하세요."))
eng2 = int(input("영어 점수를 입력하세요."))
math2 = int(input("수학 점수를 입력하세요."))
total2 = kor2+eng2+math2
avg2 = (kor2+eng2+math2)/3

name3 = input("이름을 입력하세요.")
kor3 = int(input("국어 점수를 입력하세요."))
eng3 = int(input("영어 점수를 입력하세요."))
math3 = int(input("수학 점수를 입력하세요."))
total3 = kor3+eng3+math3
avg3 = (kor3+eng3+math3)/3

print(" "*15+"학생 성적 프로그램")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,total,avg))
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name2,kor2,eng2,math2,total2,avg2))
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name3,kor3,eng3,math3,total3,avg3))
