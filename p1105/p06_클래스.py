# 기본변수 - 1개 값을 저장 - int, float, str, bool
# 복합변수 - 여러 개의 값을 저장 - list, dict, tuple, set
# 클래스 - 여러 개의 변수, 여러 개의 함수까지 저장 - class

# 클래스 사용시 장점 - 변수,함수 함께 저장, 변수에 접근 제한 가능, 한번에 여러 개의 변수, 여러 개의 함수를 바로 사용가능
# 동일한 변수를 묶음

# def 함수명:
#     프로그램

# class 이름: # 이름의 첫글자는 대문자
#     프로그램

class Car:
    
    # Car() 객체선언할 때 __init__ 함수 호출 - 생성자
    def __init__(self,color,speed):
        self.color = color # 전역변수에 없을 시 자동으로 생성함.
        self.speed = speed
    
    def upSpeed(self,speed): # 지역변수
        self.speed += speed

# 클래스를 사용하려면(변수 및 함수 호출 / 변수 값 입력), 무조건 객체선언을 해야 함.
# 객체선언
# 참조변수명 = 클래스명()

c = Car("white",10) # c라는 참조변수
# 값 읽기 - 참조변수명.변수명
print(c.color)
# 값 수정 - 참조변수명.변수명 = 값입력
c.color = "red"
print(c.color)

c2 = Car("red",100)
c2.upSpeed(100)
print(c2.speed)

# a = [12,30,20]
# a[0] = 50
# print(a)

# aa = input("시간을 입력하세요.>> ")
# if int(aa)>24:
    # print("에러입니다.")
    # 프로그램 종료
# a[0] = aa

# class cal:
#     __hour = 12 # 접근제한(private)
#     minute = 30
#     second = 20
    
#     def setHour(self,hour):
#         if hour>23: # 23:59:59 -> 00:00:00
#             print("23보다 큰 수는 입력을 할 수 없습니다.")
#             return
#         self.__hour = hour
#     def getHour(self):
#         return self.__hour

# time = cal()
# time.minute = 100
# print(time.minute)
# # print(time.__hour) # 클래스의 변수에 직접 접근 제한
# time.setHour(50)
# print(time.getHour())
