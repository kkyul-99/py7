import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,270,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
titles = ['번호','이름','국어','영어','수학','합계','평균']
stu_count = 10104

# 학생성적입력,출력,수정,삭제를 구현하시오.

while True:
    print(" "*15,"[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*60)
    choice = int(input("실행할 항목을 선택하세요.>> "))
    print()
    
    # 1. 학생성적입력
    if choice == 1:
        print(" "*15,"[ 학생 성적 입력 ]")
        print()
        name = input("{}번 학생의 이름을 입력하세요: ".format(stu_count))
        stu_count += 1
        kor = int(input("국어 점수를 입력하세요: "))
        eng = int(input("영어 점수를 입력하세요: "))
        math = int(input("수학 점수를 입력하세요: "))
        total = kor + eng + math
        avg = total / 3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        print()
        print("입력이 완료되었습니다.")
        print()
    elif choice == 2:
        print(" "*15,"[ 학생 성적 출력 ]")
        print()
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*60)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))
        print()
    elif choice == 3:
        print(" "*15,"[ 학생 성적 수정]")
        print()
        for idx,stus in enumerate(stu_list):
            print("{}. {} {}".format(idx+1,stus[0],stus[1]))
        print("-"*60)
        choice = int(input("성적을 수정할 학생을 고르세요.>> "))
        print()
        print(" "*15,"[ {} 학생 수정 과목 선택]".format(stu_list[choice-1][1]))
        print()
        print("1. 국어 점수")
        print("2. 영어 점수")
        print("3. 수학 점수")
        print("-"*60)
        subject = int(input("성적을 수정할 과목을 고르세요.>> "))
        print()
        print("현재 점수: {}".format(stu_list[choice-1][subject+1]))
        print()
        score = int(input("수정할 점수를 입력하세요.>> "))
        print()
        stu_list[choice-1][subject+1] = score
        stu_list[choice-1][5] = stu_list[choice-1][2] + stu_list[choice-1][3] + stu_list[choice-1][4]
        stu_list[choice-1][6] = stu_list[choice-1][5] / 3
        print("수정이 완료되었습니다.")
        print()
    elif choice == 4:
        print(" "*15,"[ 학생 성적 삭제 ]")
        print()
        for idx,stus in enumerate(stu_list):
            print("{}. {} {}".format(idx+1,stus[0],stus[1]))
        print("-"*60)
        choice = int(input("성적을 삭제할 학생을 고르세요.>> "))
        print()
        flag = int(input("정말 '{} {} 학생'의 성적을 삭제하시겠습니까?(1. Y 2. N)>> ".format(stu_list[choice-1][0],stu_list[choice-1][1])))
        print()
        if flag == 1:
            del stu_list[choice-1]
            print("삭제가 완료되었습니다.")
            print()
        if flag == 2:
            print("삭제가 취소되었습니다.")
            print()
    elif choice == 0:
        print()
        print("프로그램이 종료되었습니다.")
        print()
        print()
        break
