# i = i + 1   <->   i += 1
# i++ (X)

# while
stu_list = []
titles = ['이름','국어','영어','수학','합계','평균']

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요.>> "))
    print()
    ### 0. 프로그램종료
    if num == 0:
        break
    ### 1. 학생성적입력
    elif num == 1:
        print("[ 학생성적입력 ]")
        name = input("이름을 입력하세요: ")
        kor = int(input("국어 점수를 입력하세요: "))
        eng = int(input("영어 점수를 입력하세요: "))
        math = int(input("수학 점수를 입력하세요: "))
        total = kor + eng + math
        avg = total / 3
        stu_list.append([name,kor,eng,math,total,avg])
        print()
    ### 2. 학생성적출력
    elif num == 2:
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(*stus))
        print()
    ### 3. 학생성적수정
    elif num == 3:
        # 수정할 대상 선정
        print("[ 학생성적수정 ]")
        print("1. 홍길동")
        print("2. 유관순")
        print("3. 이순신")
        print("-"*50)
        num = int(input("수정하려는 학생 번호를 입력하세요.>> "))
        print()
        # 수정할 과목 선정
        print("[ {} 학생 선택 ]".format(stu_list[num-1][0]))
        print("1. 국어 성적 수정")
        print("2. 영어 성적 수정")
        print("3. 수학 성적 수정")
        print("-"*50)
        subject = int(input("수정할 과목을 선택하세요.>> "))
        print()
        # 수정할 점수 입력
        print("[ {} 학생 {} 점수 수정 ]".format(stu_list[num-1][0],titles[subject]))
        print("현재 {} 점수: {}".format(titles[subject],stu_list[num-1][subject]))
        score = int(input("수정할 {} 점수를 입력하세요: ".format(titles[subject])))
        stu_list[num-1][subject] = score
        stu_list[num-1][4] = stu_list[num-1][1]+stu_list[num-1][2]+stu_list[num-1][3] # 합계
        stu_list[num-1][5] = stu_list[num-1][4]/3 # 평균
        print()

# ### 5번 동안 숫자를 입력받아 합계를 출력하시오.
# # 1. for
# sum = 0
# for i in range(5):
#     num = int(input("숫자를 입력하세요."))
#     sum = sum + num
# print("합계: ",sum)

# # 2. while
# sum = 0
# i = 0
# while i < 5:
#     num = int(input("숫자를 입력하세요."))
#     sum = sum + num
#     i = i + 1
# print("합계: ",sum)

# ### 1 ~ 10까지 합을 구하시오.
# # 1. for
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

# # 2. while
# sum = 0
# i = 1
# while i < 11:
#     sum = sum + i
#     i = i + 1 # 증감식 - 추가
# print(sum)
