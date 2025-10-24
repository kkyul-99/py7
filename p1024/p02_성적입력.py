# 국어,영어,수학점수를 입력받아 합계와 평균을 출력하시오.

kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
print("합계 :",kor+eng+math)
# print("평균 :",(kor+eng+math)/3)
print("평균 : %.2f" % ( (kor+eng+math)/3 ) )
