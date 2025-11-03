# return: 함수를 호출한 곳으로 값을 전달할 때 사용
def cal(a,b):  # 매개변수는 꼭 타입을 일치시켜야 함
               # a,b 타입 - int,int
    return a+b # 함수 끝을 만나면 함수 종료.
    # return   # return을 만나면 함수 종료.

num1 = cal(10,5)
num2 = cal(2,7)
num3 = cal(3,5)
num4 = cal("a",5) # str,int - 에러

# 3개의 계산의 더하기, 빼기를 구하시오.
print(num1 + num2 + num3)
print(num1 - num2 - num3)
