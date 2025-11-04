# 클래스 선언
# __init__ 함수 사용
class Student:
    def __init__(self,stuno,name,kor,eng,math): # 생성자 - 객체 선언 시 바로 실행되는 함수
        self.stuno = stuno # 클래스에서 사용하는 전역변수 = 함수 내에 사용하는 지역변수
        self.name = name   # 클래스 밖에서 함수를 통해 생성된 변수를 클래스에 추가한다는 의미
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    # 합계값 변경 함수
    def total_f(self):
        self.total = self.kor+self.eng+self.math
    # 평균값 변경 함수
    def avg_f(self):
        self.avg = self.total/3

# 매개변수 __init__() 함수의 매개변수 개수와 맞아야 함.
s = Student(10101,'홍길동',80,80,80) # init을 실행시켜 s 안에 값 저장
print("국어:",s.kor)   # 80
print("합계:",s.total) # 240
s.kor = 100
print("국어:",s.kor)   # 100
s.total_f()
print("합계:",s.total) # 260

# # ------------------------------
# # 클래스 선언
# class Student:
#     pass
# s = Student     # 객체 선언 - 클래스 내 공간 생성
# s.stuno = 10101 # 변수 추가
# print(s.stuno)  # 변수 출력

# # ------------------------------
# stuno = 10101
# print(stuno)
