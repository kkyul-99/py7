# 함수를 여기에 생성
# 함수 내에 사용할 때 단순변수, 복합변수에 따라 호출 달라짐.
# 단순변수를 호출해서 값 변경 시: global
# 복합변수는 호출해서 값 변경 가능

stu_list = [
    [10101,'홍길동',80,80,80,240,80.00,0],
    [10102,'유관순',90,90,90,270,90.00,0],
    [10103,'이순신',100,100,100,300,100.00,0]
]
titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
stu_count = 10104 # 학생번호 - 단순변수

# 화면출력 함수
def screen_print():
    print("-"*60)
    print(" "*15,"[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 등수처리")
    print("0. 프로그램종료")
    print("-"*60)

# 1. 학생성적입력 함수
def stu_input():
    global stu_count # 전역변수 사용
    print(" "*15,"[ 학생 성적 입력 ]")
    print("-"*60)
    name = input("{}번 학생 이름을 입력하세요: ".format(stu_count))
    kor = int(input("국어 점수를 입력하세요: "))
    eng = int(input("영어 점수를 입력하세요: "))
    math = int(input("수학 점수를 입력하세요: "))
    total = kor + eng + math
    avg = total / 3
    stu_list.append([stu_count,name,kor,eng,math,total,avg,0])
    stu_count += 1 # 학생번호 1씩 증가
    print()
    print("성적 입력이 완료되었습니다.")
    print()

# 2. 학생성적출력 함수
def stu_print():
    print(" "*15,"[ 학생 성적 리스트 ]")
    print("-"*60)
    print(*titles,sep="\t")
    print("-"*60)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*stus))
    print()

# 3. 학생성적수정 함수
def stu_modify():
    print(" "*15,"[ 학생 성적 수정 ]")
    print("-"*60)
    for idx,stus in enumerate(stu_list):
        print("{}. {} {}".format((idx+1),stus[0],stus[1]))
    print("-"*60)
    choice = int(input("수정하려는 번호를 입력하세요.>> "))
    print()
    print(" "*15,"[ {} 학생 수정 과목 선택 ]".format(stu_list[choice-1][1]))
    print("-"*60)
    print("1. 국어 점수")
    print("2. 영어 점수")
    print("3. 수학 점수")
    print("-"*60)
    subject = int(input("수정하려는 과목을 선택하세요.>> "))
    print()
    # 0(= choice-1) [10101,'홍길동',80(= subject+1),80,80,240,80.00]
    print("-"*60)
    print("현재 {} 점수: {}".format(titles[subject+1],stu_list[choice-1][subject+1]))
    print("-"*60)
    # 점수 수정
    score = int(input("수정할 점수를 입력하세요.>> "))
    stu_list[choice-1][subject+1] = score
    # 합계 수정
    stu_list[choice-1][5] = stu_list[choice-1][2]+stu_list[choice-1][3]+stu_list[choice-1][4]
    # 평균 수정
    stu_list[choice-1][6] = stu_list[choice-1][5]/3
    print()
    print("{} 점수가 {}점으로 수정이 완료되었습니다.".format(titles[subject+1],score))
    print()
    print(stu_list[choice-1])
    print()

# 4. 학생성적삭제 함수
def stu_delete():
    print(" "*15,"[ 학생 성적 삭제 ]")
    for idx,stus in enumerate(stu_list):
        print("{}. {} {}".format((idx+1),stus[0],stus[1]))
    print("-"*60)
    choice = int(input("삭제하려는 번호를 입력하세요.>> "))
    print()
    flag = int(input("{} {} 학생이 맞습니까?(1. yes, 2. no)>> ".format(stu_list[choice-1][0],stu_list[choice-1][1])))
    print()
    if flag == 1:
        del stu_list[choice-1]
        print("삭제가 완료되었습니다.")
        print()
    if flag == 2:
        print("삭제가 취소되었습니다.")
        print()
        return # 함수에서 종료 시 return 사용, 반복문에서 멈춤: continue

# 5. 등수처리 함수
def rank():
    for s1 in stu_list:
        count = 1
        for s2 in stu_list:
            if s1[5] < s2[5]:
                count += 1
        s1[7] = count
    print()
    print("등수처리가 완료되었습니다.")
    print()

# 0. 프로그램종료 함수
def exit():
    print()
    print("[ 프로그램을 종료합니다. ]")
    print()
    print()
