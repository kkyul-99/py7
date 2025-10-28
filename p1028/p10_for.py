# # 중첩 for문 - for문을 2번 사용
# for i in range(2,10):
#     # print("[ {} 단 ]".format(i))
#     if i%2 != 0:
#         continue # 1번만 제외(9번 실행) cf) break: 완전 중지
#     for j in range(1,10):
#         # print(i,"*",j,"=",i*j)
#         print("{} X {} = {}".format(i,j,i*j))
#     # print()

# # 중첩 for문을 사용해서 00,01,02,03,...,11,12,13,...,99
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print(f"{i}{j}{k}",end=" ")

# # 1. 501 ~ 1000까지 홀수의 합을 출력하시오.
# sum1 = 0
# for i in range(501,1001):
#     if i%2 == 1:
#         sum1 = sum1 + i
# print("합계 :",sum1)

# # 2. 1 ~ 100까지 3의 배수의 합을 출력하시오.
# sum2 = 0
# for i in range(0,101,3):
#     sum2 = sum2 + i
# print("합계 :",sum2)

# enumerate(리스트) - 리스트 번호, 리스트 값
fruits = ['사과','배','복숭아','딸기','포도']
for i,fruit in enumerate(fruits):     # enumerate() 함수: index 번호 리턴
    print("{}. {}".format(i+1,fruit)) # 1. 사과 2. 배 3. 복숭아

print("[ 과일리스트 - range ]")
# for i in range(5):
for i in range(len(fruits)):
    print("{}. {}".format(i+1,fruits[i]))
