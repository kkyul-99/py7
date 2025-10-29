stu_list = []
# ['홍길동',100,90,80,270,90.00]
while True:
    name = input("이름을 입력하세요.")
    kor = int(input("국어 점수를 입력하세요."))
    eng = int(input("영어 점수를 입력하세요."))
    math = int(input("수학 점수를 입력하세요."))
    total = kor + eng + math
    avg = total / 3
    # stu_list.append(name)
    # stu_list.append(kor)
    # stu_list.append(eng)
    # stu_list.append(math)
    # stu_list.append(total)
    # stu_list.append(avg)
    stu_list = [name,kor,eng,math,total,avg]
    print()
    print("이름\t국어\t영어\t수학\t합계\t평균")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stu_list))
    print()




