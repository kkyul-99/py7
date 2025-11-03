# 함수사용목적 - 반복제거, 유지보수 편의성, 코드관리 편의성

# cal() 함수생성해서 입력받은 두 숫자사이의 합을 출력하시오.
# 함수정의
def cal(num1,num2):
    sum = 0
    for i in range(num1,num2+1):
        sum += i
    print(sum)
    
# 함수호출
num1 = int(input("숫자를 입력하세요.>> "))
num2 = int(input("숫자를 입력하세요.>> "))
cal(num1,num2)

# # 함수를 사용
# # 두 수와 + - * / 4개 중에 1개를 입력받아 결과를 출력하시오.
# def cal(a,b,c):
#     if c == '+':
#         print("{} {} {} = {}".format(a,c,b,a+b))
#     elif c == '-':
#         print("{} {} {} = {}".format(a,c,b,a-b))
#     elif c == '*':
#         print("{} {} {} = {}".format(a,c,b,a*b))
#     elif c == '/':
#         print("{} {} {} = {:.2f}".format(a,c,b,a/b))
    
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# str1 = input("원하는 사칙연산 기호를 입력하세요.(+,-,*,/)>> ")

# cal(num1,num2,str1)

# # 입력한 글자를 입력한 숫자만큼 반복 출력
# # ex) 안녕하세요 3

# def s_print(str1,num):
#     for i in range(num):
#         print(str1)

# str1 = input("글자를 입력하세요.>> ")
# num = int(input("반복 횟수를 입력하세요.>> "))
# s_print(str1,num)
