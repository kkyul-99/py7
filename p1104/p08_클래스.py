from p08_S_func import *

s1 = Student(10101,'홍길동',80,80,80)
s2 = Student(10102,'유관순',90,90,90)
s3 = Student(10103,'이순신',100,100,100)

# 학생 성적들 저장
students = Stuscore() # 객체선언
students.add(s1) # 홍길동
students.add(s2) # 유관순
students.add(s3) # 이순신

students.print()
