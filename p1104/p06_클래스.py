# 일반변수 - 숫자(정수,실수), 문자열, 불(True, False)
#         - 1개 값만 저장
# 복합변수 - 리스트, 딕셔너리, 튜플, 세트
#         - 여러 값 저장

# 클래스(객체지향언어): 변수들, 함수들을 함께 묶음 - 고급언어
# 이름, 국어, 영어, 수학 - 평균을 구하는 함수, 합계 함수

# 함수
# def 함수명():
#   프로그래밍

# 클래스 - 변수, 함수
# class 클래스명:
#   프로그래밍

# 클래스 장점:
# 1. 변수, 함수를 함께 묶음
# 2. 여러개 변수, 여러개 함수를 객체선언으로 동시 생성 가능
# 3. 각각의 변수에 값을 제한할 수 있음 - 값제한, 접근제한

class Student:
    hour = 1
    minute = 0
    second = 0 # 변수 미리 지정
    
    # 생성자 - 함수를 호출하지 않아도 객체선언 시 자동으로 호출
    def __init__(self):
        pass

# 변수 = class명: 객체선언 - class 공간을 만들어줌.
s = Student

# s = Student()   # 객체선언
# s.hour = 1    # hour 변수를 추가하는 방법
# s.minute = 2  # 클래스 접근: 참조변수.변수명 생성
# s.second = 3  # 호출 방법: 참조변수.변수명 값수정
# print(s.hour,s.minute,s.second) # 변수 읽어오기: 참조변수.변수명 검색

# s2 = Student() # 객체선언
# s2.hour = 1
# s2.minute = 2
# s2.second = 3

# s3 = Student()
# print(s3.hour)

# time_list = [1,2,3]
# time_list[0] = 50
# print(time_list)

# a = 1
# b = 2
# c = 3

# def cal(a,b,c,d,e,f,g,h,i,j...):
#     pass

# a_list = [1,2,3,4,5,6,7,8,9,10]

# def cal2(a_list):
#     pass
