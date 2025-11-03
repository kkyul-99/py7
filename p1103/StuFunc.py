import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00],
    [10102,'유관순',90,90,90,270,90.00],
    [10103,'이순신',100,100,100,300,100.00]
]
titles = ['번호','이름','국어','영어','수학','합계','평균']
stu_count = 10104 # 학생번호

def screen_print():
    print("-"*55)
    print(" "*15,"[ 학생성적프로그램 ]")
    print("-"*55)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*55)
    
def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    # global stu_count # 전역변수
    # stu_count = 10104 # 학생번호
    print(" "*15,"[ 학생 성적 입력 ]")
    print("-"*55)
    name = input("{}번 학생 이름을 입력하세요: ".format(stu_count))
    kor = int(input("국어 점수를 입력하세요: "))
    eng = int(input("영어 점수를 입력하세요: "))
    math = int(input("수학 점수를 입력하세요: "))
    total = kor + eng + math
    avg = total / 3
    stu_list.append([stu_count,name,kor,eng,math,total,avg])
    stu_count += 1 # 학생번호 1씩 증가
    print()
    print("성적 입력이 완료되었습니다.")
    print()

def stu_print():
    print(" "*15,"[ 학생 성적 리스트 ]")
    print("-"*55)
    print(*titles,sep="\t")
    print("-"*55)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))
    print()

def stu_modify():
    print(" "*15,"[ 학생 성적 수정 ]")
    print("-"*55)
    for idx,stus in enumerate(stu_list):
        print("{}. {} {}".format((idx+1),stus[0],stus[1]))
    print("-"*55)
    choice = int(input("수정하려는 번호를 입력하세요.>> "))
    print()
    print(" "*15,"[ {} 학생 수정 과목 선택 ]".format(stu_list[choice-1][1]))
    print("1. 국어 점수")
    print("2. 영어 점수")
    print("3. 수학 점수")
    print("-"*55)
    subject = int(input("수정하려는 과목을 선택하세요.>> "))
    print()
    print("-"*55)
    print("현재 {} 점수: {}".format(titles[subject+1],stu_list[choice-1][subject+1]))
    print("-"*55)
    # 점수 수정
    score = int(input("수정할 점수를 입력하세요.>> "))
    stu_list[choice-1][subject+1] = score
    # 합계 수정 
    stu_list[choice-1][5] = stu_list[choice-1][2]+stu_list[choice-1][3]+stu_list[choice-1][4]
    # 평균 수정
    stu_list[choice-1][6] = stu_list[choice-1][5]/3
    print()
    print("{} 점수가 {}점으로 수정이 완료되었습니다.".format(titles[subject+1],score))
    print(stu_list)
    print()

# def stu_delete():
#     print(" "*15,"[ 학생 성적 삭제 ]")
#     print("-"*55)
#     for idx,stus in enumerate(stu_list):
#         print("{}. {} {}".format((idx+1),stus[0],stus[1]))
#     choice = int(input("삭제하려는 번호를 입력하세요.>> "))
#     print()
#     flag = int(input("{} {} 학생이 맞습니까?(1. yes, 2. no)>> ".format(stu_list[choice-1][0],stu_list[choice-1][1])))
#     print()
#     if flag == 1:
#         del stu_list[choice-1]
#         print("삭제가 완료되었습니다.")
#         print()
#         print(stu_list)
#         print()
#     if flag == 2:
#         print("삭제가 취소되었습니다.")
#         print()
#         continue

# def stu_exit():
#     print()
#     print("[ 프로그램을 종료합니다. ]")
#     print()
#     print()
#     break
