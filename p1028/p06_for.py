### 반복문 - for문, while(): 여러 번 실행
# cf) 조건문 - if문

# range - 범위
# range(시작,끝-1,스탭) ex) range(끝): 0 ~ 끝-1
# cf) 문자열/리스트 슬라이싱 - [시작:끝-1:스탭]
for i in range(10): # 0 ~ 10-1
    print(i)

for i in range(5):
    print("안녕하세요.")
    
for _ in range(5):
    print("hello")

for i in range(5):
    print(i+1,"번째 안녕")
    
for i in range(1,6):
    print(i,"번째")

sum = 0
for i in range(1,11):
    sum = sum + i # 들여쓴 곳까지는 for문 내에 속하여 반복됨.
    print(i,"번째:",sum)
    # print("{} 번째: {}".format(i,sum))
    
print("총합계: ",sum)

a_list = ["홍길동",100,90,80]
for a in a_list: # a_list[0],a_list[1],a_list[2],a_list[3]
    print(a)

# 2차원 리스트 - for문 2번, 3차원 리스트 - for문 3번

name = "홍길동유관순이순신"
for i in name:
    print(i)

# range() 숫자를 입력하세요 10번출력
sum = 0
for i in range(10):
    num = int(input("{}번째 숫자를 입력하세요.".format(i+1)))
    sum = sum + num

print("합계: ",sum)
