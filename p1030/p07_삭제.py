stu_list = [
    ['홍길동',80,80,80,240,80.00],
    ['유관순',90,90,90,270,90.00],
    ['이순신',100,100,100,300,100.00]
]
titles = ['이름','국어','영어','수학','합계','평균']

# 0. 홍길동
# 1. 유관순
# 2. 이순신
# 출력을 하시오.

while True:
    print("[ 학생성적 삭제 리스트 ]")
    for idx,stus in enumerate(stu_list):
        print("{}. {}".format(idx+1,stus[0]))
    print("-"*50)
    num = int(input("삭제하려는 번호를 입력하세요.>> ")) # 1 -> 0
    del stu_list[num-1]
    print(stu_list)
