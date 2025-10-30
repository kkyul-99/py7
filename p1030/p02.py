import random

# 4 * 4 리스트 출력
a_list = list(range(1,10))
print(a_list)

# 랜덤섞기
random.shuffle(a_list)
print(a_list)

# 무한반복 실행
while True:
    print("[ 좌표 맞추기 게임]")
    print("-"*30)
    for idx,a in enumerate(a_list):
        print(a,end="\t")
        if (idx+1)%3 == 0:
            print()
    print("-"*30)
    num = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    # 9 -> 9가 X로 바뀌어야 함.
    for idx,a in enumerate(a_list):
        if a == num:
            a_list[idx] = "X"
            break
# ------------------------------
