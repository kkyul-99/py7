n_list = []
i = 0
while True:
    if i < 4:
        name = input("{}번째 이름을 입력하세요.".format(len(n_list)+1))
        kor = int(input("{}번째 국어 점수를 입력하세요.".format(len(n_list)+1)))
        n_list.append([name,kor])
        print(n_list)
    else:
        break
    i = i + 1 # while에서는 i가 저절로 늘어나지 않으므로 증감식 필요

# 전체 출력
print("[ 학생성적프로그램 ]")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
for i in range(len(n_list)):
    print("{}\t{}".format(*n_list[i]))

# n_list = []

# n_list.append(1)
# n_list.append(2)
# n_list.append(3)
# n_list.insert(0,5)
# n_list.insert(2,100)
# n_list.extend([10,20,30]) # list 타입을 추가
# n_list.append([100,200,300])
# n_list.append(['홍길동',100])
# print(n_list)
