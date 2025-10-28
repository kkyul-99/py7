# 1~5까지 for문을 사용해서 출력하시오.
for i in range(5):
    print(i+1)

# 숫자를 입력받아, 입력받은 값을 출력하는 것을 5번 반복하시오.
for i in range(5):
    print(int(input(f"{i+1}번째 숫자를 입력하시오: ")))

# 1~10까지 숫자의 합을 출력하시오. 반복 10번
total = 0
for i in range(1,11):
    total = total + i

print("합계: ",total)

# 1~10까지 홀수 합계를 구하시오.
# 1. range 스탭을 사용해서 할 것
total = 0
for i in range(1,11,2):
    total = total + i

print("합계 :",total)

# 2. if문을 사용해서 할 것
total = 0
for i in range(1,11):
    if i%2 == 1:
        total = total + i

print("합계: ",total)

# # for문
# # 구조 - for 변수 in 범위(range, list, 문자열):

# for i in range(10):
#     print(i)

# # 반갑습니다. 10번 출력하시오.
# for i in range(10):
#     print("반갑습니다.")

# n = int(input("몇 개의 숫자를 입력하시겠습니까? "))
# total = 0
# a_list = []
# for i in range(n):
#     num = int(input(f"{i+1}번째 숫자를 입력하세요: "))
#     if num%2 == 0:
#         break # 반복문을 중지시키는 명령어
#     a_list.append(num)
#     total = total + num

# print("리스트: ",a_list)
# print("총 합계: ",total)
