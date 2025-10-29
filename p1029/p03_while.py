# i = i + 1   <->   i += 1
# i++ (X)

# while
while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*50)
    no = int(input("원하는 번호를 입력하세요."))
    print()
    if no == 0:
        break
    elif no == 1:
        print("[ 학생성적입력 ]")
        stu_list = []
        while True:
            name = input("이름을 입력하세요.")
            kor = int(input("국어 점수를 입력하세요."))
            eng = int(input("영어 점수를 입력하세요."))
            math = int(input("수학 점수를 입력하세요."))
            total = kor + eng + math
            avg = total / 3
            stu_list.append([name,kor,eng,math,total,avg])
            print()
            print("이름\t국어\t영어\t수학\t합계\t평균")
            print("-"*50)
            # [[name,kor,eng,math,total,avg]]
            for i in range(len(stu_list)):
                print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stu_list[i]))
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
