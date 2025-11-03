import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,280,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
stu_count = 10104  #학생번호
titles = ['번호','이름','국어','영어','수학','합계','평균']

while True:
    print("-"*60)
    print(" "*10,"[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*60)
    choice = int(input("실행할 항목을 선택하세요.>> "))
    print()

# 학생입력부분
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

# 학생출력부분
    elif choice == 2:
        print(" "*15,"[ 학생 성적 출력]")
        print()
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*60)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))
        print()
    
    elif choice == 3:
        print(" "*15,"[ 학생 성적 수정]")
        print()
        print("-"*60)
        pass
    
    elif choice == 4:
        print(" "*15,"[ 학생 성적 삭제]")
        print()
        print("-"*60)
        for idx,stus in enumerate(stu_list):
            print("{}\t{}\t{}".format(idx+1,stu_list[0],stu_list[1]))
        
        
    elif choice == 0:
        print()
        print("프로그램이 종료되었습니다.")
        print()
        print()
        break
