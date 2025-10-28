# 이름, 국어, 영어, 수학, 합계, 평균
# 3명의 학생성적을 입력받아 stus에 모두 저장하여 출력하시오.

stus = []

name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
total = kor+eng+math
avg = total/3
stu = [name, kor, eng, math, total, avg]
stus.append(stu)

name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
total = kor+eng+math
avg = total/3
stu = [name, kor, eng, math, total, avg]
stus.append(stu)

name = input("이름을 입력하세요.")
kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
math = int(input("수학 점수를 입력하세요."))
total = kor+eng+math
avg = total/3
stu = [name, kor, eng, math, total, avg]
stus.append(stu)

print(stus)

print(stus[0])    # ['홍길동', 100, 100, 99, 299, 99.66666666666667]
print(stus[0][0]) # 홍길동
print(stus[0][1]) # 100
