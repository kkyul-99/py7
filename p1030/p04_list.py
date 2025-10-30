# a_list = [1,2,3,4,5]
# b_list = list(range(1,6))
# c_list = [i for i in range(1,6)] # 리스트 내포
# print(a_list)
# print(b_list)
# print(c_list)

# # 추가: append, insert, extend
# # 삭제: pop, del, remove, clear
# # 수정: a_list[index] = 값
# # .index(n): 해당 위치값 리턴

# aa_list = [10,5,15,7,9]
# print(aa_list.index(7))

# # 비교 ver.1
# print(aa_list) # [10,5,15,7,9]
# num = int(input("원하는 번호를 입력하세요.>> "))
# for idx,aa in enumerate(aa_list):
#     if num == aa:
#         aa_list[idx] = "X"
# print(aa_list)

# # 비교 ver.2
# print(aa_list) # [10,5,15,7,9]
# num = int(input("원하는 번호를 입력하세요.>> "))
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"
# print(aa_list)

# 5 * 5의 2차원 형태 리스트를 생성
# 좌표만들기

import random
a_list = list(range(1,26))
random.shuffle(a_list)

while True:
    print("\t\t[ B I N G O ]")
    print("-"*50)
    for idx,a in enumerate(a_list):
        print(a,end="\t")
        if (idx+1)%5 == 0:
            print()

    num = int(input("원하는 번호를 입력하세요.>> "))
    print()

    if num in a_list:
        a_list[a_list.index(num)] = "X"
