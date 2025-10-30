stu_list = [
    ['홍길동',80,80,80,240,80.00],
    ['유관순',90,90,90,270,90.00],
    ['이순신',100,100,100,300,100.00]
]
titles = ['이름','국어','영어','수학','합계','평균']

# 0. 홍길동
# 1. 유관순
# 2. 이순신
# ----------
# 수정하고 싶은 학생번호를 입력하세요.
# 국어 점수를 변경하는 프로그램을 구현하시오.

while True:
# 수정할 대상 선정
    print("[ 학생성적수정 ]")
    print("0. 홍길동")
    print("1. 유관순")
    print("2. 이순신")
    print("-"*30)
    num = int(input("수정하려는 학생 번호를 입력하세요.>> "))
    print()
# 수정할 과목 선정
    print("[ {} 학생 선택 ]".format(stu_list[num][0]))
    print("1. 국어 성적 수정")
    print("2. 영어 성적 수정")
    print("3. 수학 성적 수정")
    print("-"*50)
    subject = int(input("수정할 과목을 선택하세요.>> "))
    print()
# 수정할 점수 입력
    print("[ {} 학생 {} 점수 수정 ]".format(stu_list[num][0],titles[subject]))
    print("현재 {} 점수: {}".format(titles[subject],stu_list[num][subject]))
    score = int(input("수정할 {} 점수를 입력하세요.>> ".format(titles[subject])))
    stu_list[num][subject] = score
    stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3] # 합계
    stu_list[num][5] = stu_list[num][4]/3 # 평균
    print()

# # 1번 선택
# # 국어 점수를 70점으로 변경하고, 합계, 평균 변경해서 출력하시오.
# stu_list[1][1] = 70
# stu_list[1][4] = stu_list[1][1] + stu_list[1][2] + stu_list[1][3]
# stu_list[1][5] = stu_list[1][4]/3
# print(stu_list)

# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][1] + stu_list[2][2] + stu_list[2][3]
# stu_list[2][5] = stu_list[2][4]/3
# print(stu_list)

# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list)

# a_list = [1,2,3,4,5,6,7,8,9] # len(a_list) = 9
# b_list = [                   # len(b_list) = 3
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a_list[3] = 100
# b_list[1][0] = 100
# b_list[2][1] = 50

# # 1차원 리스트 출력
# for a in a_list:
#     print(a,end="\t")
# print()
# print("-"*50)

# for bs in b_list:
#     for b in bs:
#         print(b,end="\t")
