# # for 변수 in 범위:
# # pass - 빈 공백: for, if 한 줄이라도 코드가 없으면 에러가 나기에 입력하는 것
# # break - 반복문을 종료
# # continue - 1회 반복문을 제외시켜줌.
# for i in range(10):
#     pass  # 아무것도 일어나지 않음 - 빈 공백
#     print("프로그램 종료")
#     break # 이 시점에서 반복문을 종료 - 한 번만 실행

# for i in range(10): # 홀수만 찍힘
#     if i%2 == 0:
#         continue
#     print(i)

# for i in range(10): # 짝수만 찍힘
#     if i%2 == 0:
#         print(i)
#     continue

# for i in range(10): # 아무것도 안 찍힘
#     if i%2 == 0:
#         continue
#         print(i)

# for i in range(10): # 마지막 것만 찍힘
#     if i%2 == 0:
#         continue
# print(i)

# for i in range(2,10):
#     for j in range(1,10):
#         print("숫자: ",j)
#     print("-"*50)

# for i in range(2,10): # 8 - 2,3,4,5,6,7,8,9
#     print(i)

# for i in range(8):    # 8 - 0,1,2,3,4,5,6,7
#     print(i)

# # 5,21출력하시오.
# for i in range(5,22):
#     print(i)

# # 1,10까지 출력하시오.
# for i in range(1,11):
#     print(i)

# # 0,9까지 출력하시오. 홀수만 출력하시오.
# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)

# # 구구단을 출력하시오.
# for i in range(2,10):
#     if i%2 == 0:
#         continue
#     print("[ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print()

# # for 변수 in 범위: -> range, list, 문자열, 딕셔너리, 튜플
# names = ['홍길동','유관순','이순신','김구','강감찬']
# for name in names:
#     print(name) # 1. 홍길동 2. 유관순 ...

# for i,name in enumerate(names): # index 번호, 값을 함께 리턴
#         # print(name[0],name[1])
#         print("{}. {}".format(i+1,name))

# n_list = [
#     [1,'홍길동'],
#     [2,'유관순'],
#     [3,'이순신']
# ]
# for ns in n_list: # [1,'홍길동'],[2,'유관순'],[3,'이순신']
#     for n in ns:
#         print(n,end="")
#     print()


a_list = []
# for문을 사용해서 0이 10개 들어가는 리스트를 만드시오.
for i in range(10):
    a_list.append('0')
print(a_list)

a_list = list('0'*10)
print(a_list)

# 리스트 내포
a_list = [0 for i in range(10)]
print(a_list)

a_list = [i*i for i in range(1,10)]
print(a_list)
