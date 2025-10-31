### 영어맞추기 프로그램을 구현하시오.
### 1:정답 2:오답 3:오답 4:정답 5:정답
### 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오.
import random

english = {
    '사랑':'love','차':'car','커피':'coffee','전화':'phone','컴퓨터':'computer',
    '이름':'name','한국':'korea','물':'water','지구':'earth','하늘':'sky',
    '공기':'air','고양이':'cat','강아지':'dog','아기':'baby','엄마':'mother',
    '아빠':'father','집':'house','소년':'boy','소녀':'girl','열쇠':'key'
}

a_list = range(20)
quest = random.sample(a_list,5) # 랜덤 5개 - 20문제 중 5개를 추출
quest.sort()                    # 랜덤 5개를 순서대로 정렬
quest_dict = {}                  # 정답, 오답 입력을 위한 저장공간
count = 0
num = 0

for i,k in enumerate(english.keys()): # index, key를 함께 추출
    if i in quest:
        # 정답입력
        print("{} 은(는) 영어로 뭘까요? ".format(k))
        answer = input(">> ")
        num += 1
        # 정답확인
        if answer == english[k]:
            print("정답입니다!")
            count += 1
            quest_dict[num] = "정답"
        else:
            print("오답입니다. 정답: {}".format(english[k]))
            quest_dict[num] = "오답"
        print()

print(quest_dict)
print("정답: ",count,"개")

# --------------------------------------------------
k = list(english.keys())
v = list(english.values())
r_qst = random.sample(k,5)

count = 0
num = 0
c_dict = {}

for i in r_qst:
    print("{} 은(는) 영어로 뭘까요?".format(i))
    ans = input(">> ")
    num += 1
    if ans == english[i]:
        print("정답입니다.")
        count += 1
        c_dict[num] = "정답"
    else:
        print("오답입니다. 정답: {}".format(english[i]))   
        c_dict[num] = "오답" 
    print()

print(c_dict)
print("정답개수: {} 개".format(count))

# --------------------------------------------------
r_qst = random.sample(list(english.items()),5)

for i in r_qst:
    print("{} 은(는) 영어로 뭘까요?".format(i[0]))
    ans = input(">> ")
    if ans == i[1]:
        print("정답입니다.")
    else:
        print("오답입니다. 정답: {}".format(i[1]))
    print()
